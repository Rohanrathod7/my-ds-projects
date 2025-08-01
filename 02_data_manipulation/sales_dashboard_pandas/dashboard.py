import pandas as pd

def total_sales(df):
    return df["Sales"].sum()

def sales_by_product(df):
    return df.groupby("Product.Name")["Sales"].sum().reset_index()

def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum().reset_index()

def sales_by_category(df):
    return df.groupby("Sub.Category")["Sales"].sum().reset_index()

def monthly_sales(df):
    return df.groupby(df["Order.Date"].dt.to_period("M"))["Sales"].sum().reset_index()

def top_selling_products(df, top_n = 5):
    return df.groupby("Product.Name")["Sales"].sum().sort_values(ascending=False).head(top_n).reset_index()