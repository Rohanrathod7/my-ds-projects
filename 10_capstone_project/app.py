# app.py
# Data Science Portfolio App
# - Load real datasets (built-in, GitHub raw URL, or upload)
# - EDA & Visuals
# - Regression, Classification, Clustering (KMeans)
# - Clean, production-friendly structure

import io
import json
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from urllib.parse import urlparse

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score, confusion_matrix,
    classification_report, r2_score, mean_absolute_error, mean_squared_error
)
from sklearn.linear_model import LogisticRegression, Ridge, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


st.set_page_config(
    page_title="Data Science Portfolio App",
    page_icon="📊",
    layout="wide"
)


GITHUB_DATASETS = {
    "Seaborn Titanic (GitHub)": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv",
    "Seaborn Penguins (GitHub)": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv",
    "Seaborn Iris (GitHub)": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
    "Seaborn Tips (GitHub)": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
}

def is_url(s: str) -> bool:
    try:
        u = urlparse(s)
        return all([u.scheme in ("http", "https"), u.netloc, u.path])
    except Exception:
        return False

@st.cache_data(show_spinner=True)
def load_data(source: str, file_bytes: bytes | None = None) -> pd.DataFrame:
    if source in GITHUB_DATASETS:
        return pd.read_csv(GITHUB_DATASETS[source])
    if source == "Upload CSV" and file_bytes is not None:
        return pd.read_csv(io.BytesIO(file_bytes))
    if is_url(source):
        return pd.read_csv(source)
    raise ValueError("Invalid data source.")

def split_feature_types(df: pd.DataFrame):
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()
    return num_cols, cat_cols

def basic_eda(df: pd.DataFrame):
    st.subheader("Shape & Preview")
    c1, c2 = st.columns([1,2])
    with c1:
        st.write(f"Rows: **{df.shape[0]}**, Columns: **{df.shape[1]}**")
        st.dataframe(df.head())
    with c2:
        st.write("Missing values per column")
        st.dataframe(df.isna().sum().to_frame("missing").sort_values("missing", ascending=False))

    num_cols, cat_cols = split_feature_types(df)

    if num_cols:
        st.subheader("Numerical Summary")
        st.dataframe(df[num_cols].describe().T)

        st.subheader("Correlation Heatmap (Numerical)")
        corr = df[num_cols].corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(corr, annot=False, cmap="Blues", ax=ax)
        st.pyplot(fig)

        st.subheader("Distributions (Numerical)")
        sel_num = st.multiselect("Select numerical columns", num_cols, default=num_cols[:min(3, len(num_cols))])
        if sel_num:
            fig, ax = plt.subplots(figsize=(8,3*len(sel_num)))
            for i, col in enumerate(sel_num, 1):
                plt.subplot(len(sel_num), 1, i)
                sns.histplot(df[col].dropna(), kde=True)
                plt.title(col)
            plt.tight_layout()
            st.pyplot(fig)

    if cat_cols:
        st.subheader("Category Counts")
        sel_cat = st.multiselect("Select categorical columns", cat_cols, default=cat_cols[:min(3, len(cat_cols))])
        if sel_cat:
            fig, ax = plt.subplots(figsize=(8,3*len(sel_cat)))
            for i, col in enumerate(sel_cat, 1):
                plt.subplot(len(sel_cat), 1, i)
                sns.countplot(x=col, data=df)
                plt.xticks(rotation=30, ha='right')
                plt.title(col)
            plt.tight_layout()
            st.pyplot(fig)

def build_preprocessor(num_cols, cat_cols, scale_numeric=True):
    num_steps = [("imputer", SimpleImputer(strategy="median"))]
    if scale_numeric:
        num_steps.append(("scaler", StandardScaler()))
    num_tf = Pipeline(steps=num_steps)
    cat_tf = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    pre = ColumnTransformer(
        transformers=[
            ("num", num_tf, num_cols),
            ("cat", cat_tf, cat_cols)
        ]
    )
    return pre

def train_classification(df: pd.DataFrame):
    st.subheader("Classification")
    target = st.selectbox("Select target (categorical/binary)", df.columns)
    if target is None:
        return
    X = df.drop(columns=[target]).copy()
    y = df[target].copy()

    # ensure y is categorical
    if y.dtype.kind in "iuf":  # numeric target likely regression—allow user override
        st.info("Target appears numeric; ensure this is a classification problem (e.g., 0/1).")

    num_cols, cat_cols = split_feature_types(X)
    pre = build_preprocessor(num_cols, cat_cols, scale_numeric=True)

    model_name = st.selectbox("Model", ["Logistic Regression", "Random Forest Classifier"])
    if model_name == "Logistic Regression":
        model = LogisticRegression(max_iter=200, n_jobs=None if hasattr(LogisticRegression, "n_jobs") else None)
    else:
        model = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)

    test_size = st.slider("Test size", 0.1, 0.5, 0.2, 0.05)
    random_state = st.number_input("Random state", value=42, step=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=int(random_state), stratify=y)
    pipe = Pipeline(steps=[("pre", pre), ("model", model)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    proba_supported = hasattr(pipe, "predict_proba")
    st.write("**Accuracy**:", round(accuracy_score(y_test, y_pred), 4))
    try:
        st.write("**F1 (macro)**:", round(f1_score(y_test, y_pred, average="macro"), 4))
    except Exception:
        pass

    # ROC-AUC for binary only
    if proba_supported and len(np.unique(y_test)) == 2:
        y_prob = pipe.predict_proba(X_test)[:, 1]
        try:
            st.write("**ROC-AUC**:", round(roc_auc_score(y_test, y_prob), 4))
        except Exception:
            pass

    st.write("**Confusion Matrix**")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", ax=ax)
    st.pyplot(fig)

    st.write("**Classification Report**")
    st.code(classification_report(y_test, y_pred))

    # Feature importance (if available)
    try:
        model_obj = pipe.named_steps["model"]
        pre_obj = pipe.named_steps["pre"]
        if hasattr(model_obj, "feature_importances_"):
            # map back feature names
            oh = pre_obj.named_transformers_["cat"].named_steps["onehot"]
            cat_names = oh.get_feature_names_out(pre_obj.transformers_[1][2])
            num_names = pre_obj.transformers_[0][2]
            feat_names = np.concatenate([num_names, cat_names])
            importances = pd.Series(model_obj.feature_importances_, index=feat_names).sort_values(ascending=False)[:20]
            st.write("**Top Feature Importances**")
            fig, ax = plt.subplots(figsize=(7,5))
            sns.barplot(x=importances.values, y=importances.index, ax=ax)
            st.pyplot(fig)
    except Exception:
        pass

def train_regression(df: pd.DataFrame):
    st.subheader("Regression")
    target = st.selectbox("Select target (numeric)", df.columns)
    if target is None:
        return
    if df[target].dtype.kind not in "iuf":
        st.warning("Selected target is not numeric.")
        return

    X = df.drop(columns=[target]).copy()
    y = df[target].copy()
    num_cols, cat_cols = split_feature_types(X)
    pre = build_preprocessor(num_cols, cat_cols, scale_numeric=True)

    model_name = st.selectbox("Model", ["Linear Regression", "Ridge", "Random Forest Regressor"])
    if model_name == "Linear Regression":
        model = LinearRegression()
    elif model_name == "Ridge":
        alpha = st.slider("Ridge alpha", 0.01, 10.0, 1.0, 0.01)
        model = Ridge(alpha=alpha, random_state=42)
    else:
        n_estimators = st.slider("RF n_estimators", 100, 600, 300, 50)
        model = RandomForestRegressor(n_estimators=n_estimators, random_state=42, n_jobs=-1)

    test_size = st.slider("Test size", 0.1, 0.5, 0.2, 0.05, key="reg-ts")
    random_state = st.number_input("Random state", value=42, step=1, key="reg-rs")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=int(random_state))
    pipe = Pipeline(steps=[("pre", pre), ("model", model)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    st.write("**R²**:", round(r2_score(y_test, y_pred), 4))
    st.write("**MAE**:", round(mean_absolute_error(y_test, y_pred), 4))
    st.write("**RMSE**:", round(np.sqrt(mean_squared_error(y_test, y_pred)), 4))

    # Pred vs True plot
    fig, ax = plt.subplots(figsize=(5,4))
    sns.scatterplot(x=y_test, y=y_pred, ax=ax)
    ax.set_xlabel("True")
    ax.set_ylabel("Predicted")
    ax.set_title("Predicted vs True")
    st.pyplot(fig)

def run_clustering(df: pd.DataFrame):
    st.subheader("Clustering (KMeans)")
    # Use only numeric features for clustering
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not num_cols:
        st.warning("No numeric columns available for KMeans.")
        return

    subset_cols = st.multiselect("Select numeric columns for clustering", num_cols, default=num_cols[:min(6, len(num_cols))])
    if not subset_cols:
        return
    X = df[subset_cols].copy()
    imputer = SimpleImputer(strategy="median")
    X_imp = imputer.fit_transform(X)

    k = st.slider("Number of clusters (k)", 2, 10, 3, 1)
    km = KMeans(n_clusters=k, random_state=42, n_init="auto")
    clusters = km.fit_predict(X_imp)

    st.write("**Inertia**:", round(km.inertia_, 2))
    try:
        sil = silhouette_score(X_imp, clusters)
        st.write("**Silhouette Score**:", round(sil, 4))
    except Exception:
        pass

    # PCA 2D visualization
    pca = PCA(n_components=2, random_state=42)
    X2 = pca.fit_transform(X_imp)
    viz = pd.DataFrame({"pc1": X2[:,0], "pc2": X2[:,1], "cluster": clusters})
    fig, ax = plt.subplots(figsize=(6,5))
    sns.scatterplot(data=viz, x="pc1", y="pc2", hue="cluster", palette="tab10", ax=ax)
    ax.set_title("Clusters in 2D (PCA)")
    st.pyplot(fig)

    st.write("**Cluster sizes**")
    st.dataframe(pd.Series(clusters).value_counts().rename("count"))

# ---------- Sidebar ----------
st.sidebar.title("📦 Data Science Portfolio App")
st.sidebar.markdown("**Load a dataset** and explore EDA, models, and clustering.")

data_source_choice = st.sidebar.selectbox(
    "Choose data source",
    list(GITHUB_DATASETS.keys()) + ["Upload CSV", "Paste GitHub Raw CSV URL"]
)

uploaded_file = None
custom_url = None
if data_source_choice == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload a CSV", type=["csv"])
elif data_source_choice == "Paste GitHub Raw CSV URL":
    custom_url = st.sidebar.text_input("Raw CSV URL (https://raw.githubusercontent.com/...)")

st.sidebar.markdown("---")
st.sidebar.caption("Tip: Start with **Seaborn Titanic** or **Penguins**.")

# ---------- Load data ----------
df = None
try:
    if data_source_choice in GITHUB_DATASETS:
        df = load_data(data_source_choice)
    elif data_source_choice == "Upload CSV" and uploaded_file is not None:
        df = load_data(data_source_choice, uploaded_file.getvalue())
    elif data_source_choice == "Paste GitHub Raw CSV URL" and custom_url and is_url(custom_url):
        df = load_data(custom_url)
except Exception as e:
    st.sidebar.error(f"Failed to load dataset: {e}")

# ---------- Main ----------
st.title("📊 Data Science Portfolio App")
st.write("A single web app that demonstrates **EDA, Visuals, Regression, Classification, and Clustering** on real datasets.")

tabs = st.tabs(["📥 Data", "🧭 EDA", "🧠 Modeling", "🌐 Clustering", "📝 Insights"])

with tabs[0]:
    st.header("Load & Inspect Data")
    st.markdown("Select a built-in dataset, paste a **GitHub raw CSV URL**, or upload your own file.")
    if df is not None:
        st.success("Dataset loaded ✅")
        st.dataframe(df.head())
        st.write("Column dtypes:")
        st.json({c: str(t) for c, t in df.dtypes.items()})
    else:
        st.info("No dataset loaded yet. Use the sidebar to select or upload data.")

with tabs[1]:
    st.header("Exploratory Data Analysis")
    if df is not None:
        basic_eda(df)
    else:
        st.warning("Load a dataset first.")

with tabs[2]:
    st.header("Supervised Modeling")
    if df is not None:
        task = st.radio("Choose a task", ["Classification", "Regression"], horizontal=True)
        if task == "Classification":
            train_classification(df)
        else:
            train_regression(df)
    else:
        st.warning("Load a dataset first.")

with tabs[3]:
    st.header("Unsupervised Clustering")
    if df is not None:
        run_clustering(df)
    else:
        st.warning("Load a dataset first.")

with tabs[4]:
    st.header("Insights & Structure")
    st.markdown("""
- **Data Loading:** Built-in public datasets or your own CSV (upload or GitHub raw link).
- **Cleaning:** Automatic imputation of missing values; encoding categories; scaling numerics in pipelines.
- **EDA:** Shape, preview, missingness, numeric summaries, correlations, distributions, category counts.
- **Modeling:**
  - **Classification:** Logistic Regression, Random Forest (accuracy, F1, ROC-AUC, confusion matrix, report, importances).
  - **Regression:** Linear/Ridge/RandomForest (R², MAE, RMSE + Pred vs True plot).
- **Clustering:** KMeans with k selector, inertia/silhouette, PCA 2D visualization, cluster sizes.
- **Reproducibility:** Deterministic `random_state`, cached dataset loading, clean sklearn pipelines.
    """)
