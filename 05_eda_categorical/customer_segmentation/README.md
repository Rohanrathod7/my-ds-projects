# 🧠 Customer Segmentation by Categorical Data

## Dataset
- **Mall Customers Dataset** from Kaggle (~200 entries)
- Key columns: `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1–100)`

## Goals
- Differentiate nominal vs ordinal categorical data
- Create new categories (`IncomeBracket`, `AgeGroup`)
- Explore frequencies and grouping operations
- Visualize categorical distributions and relationships
- Label encode and one-hot encode categories for modeling

## Key Concepts
- `.value_counts()` and `.groupby()`
- `pd.cut()` for binning continuous data into ordered categories
- Seaborn `catplot` visualizations
- Label encoding nominal fields, one-hot encoding ordinal categories

## Insights
- Spending Score trends across Income Brackets
- Income differences by Age Group
- Gender distribution by spending levels

## Usage
Run `segmentation_eda.ipynb` in Jupyter or Colab—each cell is explained, and visuals are inline.

## 🔍 Enhancements

- ✅ Added CLV score and CLV-based segmentation
- ✅ Cross-tab analysis of gender vs income segments
- ✅ Hypothesis testing using box plots
- ✅ Feature scaling for downstream clustering
- ✅ Added synthetic region for geosegmentation
- ✅ Cleaned inconsistent labels
- ✅ Ordinal encoding as numerical scores
- ✅ Visual exploration with `pairplot`

## 📊 Insights Generated

- CLV category strongly correlates with high-income, high-spending segments
- Female customers show higher variance in spending across all income brackets
- Geographic region influences income and age distributions

