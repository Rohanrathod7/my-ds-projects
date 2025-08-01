import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=["Order.Date", 'Ship.Date'])
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None