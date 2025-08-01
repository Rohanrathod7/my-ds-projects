# Superstore Sales Dashboard CLI

This project uses a real **Global Superstore** dataset to create a CLI-based sales dashboard using Python and Pandas.

## Features

- Total sales
- Sales breakdown by product, region, category
- Monthly sales trends
- Top-selling products by quantity

## Structure

        sales_dashboard_global/
        ├── cli.py
        ├── dashboard.py
        ├── utils.py
        ├── data/
        │ └── superstore_sales.csv
        └── README.md


## Usage

1. Download the Global Superstore dataset from Kaggle [(https://www.kaggle.com/datasets/ronysoliman/global-superstore-dataset/code)]
2. Rename the CSV and place it in `data/superstore_sales.csv`  
3. Run the dashboard:

```bash
python cli.py data/superstore_sales.csv
