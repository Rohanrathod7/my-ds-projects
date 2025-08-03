import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="📊 Enhanced CSV Processor", layout="wide")

st.title("📊 Enhanced CSV Processor with Charts & Merge")

# -- Upload one or more CSVs
uploaded_files = st.file_uploader("📁 Upload CSV file(s)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    dfs = []
    for file in uploaded_files:
        if file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            df = pd.read_csv(file)
        dfs.append(df)

    # Merge files if more than one
    if len(dfs) > 1:
        st.success(f"✅ {len(dfs)} files uploaded. Automatically merged.")
        df = pd.concat(dfs, ignore_index=True)
    else:
        df = dfs[0]
        st.success("✅ 1 file uploaded.")

    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    # Summary stats
    if st.checkbox("📈 Show Summary Statistics"):
        st.write(df.describe(include='all'))

    # Filter by column
    st.subheader("🔍 Filter Rows")
    col_to_filter = st.selectbox("Select a column to filter", df.columns)
    if pd.api.types.is_numeric_dtype(df[col_to_filter]):
        min_val = float(df[col_to_filter].min())
        max_val = float(df[col_to_filter].max())
        user_range = st.slider(f"Select {col_to_filter} range", min_val, max_val, (min_val, max_val))
        filtered_df = df[(df[col_to_filter] >= user_range[0]) & (df[col_to_filter] <= user_range[1])]
    else:
        unique_vals = df[col_to_filter].dropna().unique().tolist()
        selected_val = st.selectbox(f"Select a value from '{col_to_filter}'", unique_vals)
        filtered_df = df[df[col_to_filter] == selected_val]

    st.write(f"🧾 Filtered Data ({len(filtered_df)} rows):")
    st.dataframe(filtered_df.head())

    # Column selection
    st.subheader("🎯 Select Columns to View")
    selected_cols = st.multiselect("Pick columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(filtered_df[selected_cols].head())

    # Visualization
    st.subheader("📊 Visualize Selected Columns")
    num_cols = filtered_df[selected_cols].select_dtypes(include='number').columns.tolist()
    if len(num_cols) >= 2:
        x_axis = st.selectbox("X-axis", num_cols)
        y_axis = st.selectbox("Y-axis", [col for col in num_cols if col != x_axis])
        chart = alt.Chart(filtered_df).mark_circle(size=60).encode(
            x=x_axis, y=y_axis, tooltip=list(filtered_df.columns)
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("📌 Need at least two numeric columns for visualization.")

    # Download
    st.subheader("💾 Download Filtered Output")
    download_data = filtered_df[selected_cols]
    csv = download_data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", data=csv, file_name="filtered_output.csv", mime='text/csv')

else:
    st.info("👈 Upload one or more CSV/Excel files to get started!")
