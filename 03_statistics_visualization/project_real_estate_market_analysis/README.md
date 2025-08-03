# 📊 Real Estate Market Analysis (Ames Housing Dataset)

## Objective  
Analyze factors that influence residential property pricing using a rich, real-world dataset.

## Dataset  
- **Ames Housing Data**, featuring 79 explanatory variables and `SalePrice`.
- Covers structural, quality, neighborhood, and age-related housing attributes:contentReference[oaicite:27]{index=27}.

## Analyses Performed
- Descriptive stats & distribution visualization (including log-transformed prices)
- Imputation and encoding of categorical features
- Correlation heatmap to identify top predictors of price
- Scatter, boxplot, violin, and pair/facet grids for deeper trend analysis
- Neighborhood-level price summaries

## Key Insights
- **GrLivArea** and **OverallQual** are top drivers of price.
- Houses in certain neighborhoods command **significant price premiums** (20–30% above city median).
- Each improvement of one quality point correlates with a notable incremental price gain.

## Tools
Python (3.7+), pandas, numpy, seaborn, matplotlib

## How to Run
Open `analysis.ipynb` in Jupyter or Google Colab and execute all cells to see charts, code, and commentary.

