import argparse
from utils import load_data
from dashboard import (
    total_sales,
    sales_by_product,
    sales_by_region,
    sales_by_category,
    monthly_sales,
    top_selling_products
)

def main():
    parser = argparse.ArgumentParser(description="Sales Dashboard CLI")
    parser.add_argument("file_path", help="path to the sales data CSV file")
    file_path = parser.parse_args().file_path

    df = load_data(file_path)
    if df is not None:
        print("Total Sales:", total_sales(df))
        print("Sales by Product:\n", sales_by_product(df))
        print("Sales by Region:\n", sales_by_region(df))
        print("Sales by Category:\n", sales_by_category(df))
        print("Monthly Sales:\n", monthly_sales(df))
        print("Top Selling Products:\n", top_selling_products(df))
        print("Dashboard generated successfully.")
    else:
        print("Failed to load data. Please check the file path and try again.")

if __name__ == "__main__":
    main()  