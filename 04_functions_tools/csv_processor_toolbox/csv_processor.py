import argparse
import pandas as pd
import os
from pathlib import Path
import logging

logging.basicConfig(
    filename="processor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)




def summarize_csv(file_path):
    print(f"\n📄 Summary for: {file_path}")
    df = pd.read_csv(file_path)
    print(df.info())
    print("\n🔢 Basic Stats:")
    print(df.describe())
    logging.info(f"Summarized {file_path}")

def filter_csv(file_path, column, value):
    df = pd.read_csv(file_path)
    if column not in df.columns:
        print(f"❌ Column '{column}' not found.")
        return
    filtered = df[df[column] == value]
    print(f"\n✅ Rows where {column} == {value}: {len(filtered)}")
    print(filtered.head())
    logging.info(f"Filtered {file_path} on column {column} == {value}")

def merge_csv(files):
    dfs = [pd.read_csv(f) for f in files]
    merged = pd.concat(dfs, ignore_index=True)
    print("\n✅ Merged DataFrame Preview:")
    print(merged.head())
    return merged
    logging.info(f"Filtered {file_path} on column {column} == {value}")

def select_columns(file_path, columns):
    df = pd.read_csv(file_path)
    cols = columns.split(',')
    if not set(cols).issubset(df.columns):
        print("❌ One or more columns not found.")
        print(f"Available columns: {df.columns.tolist()}")
        return
    print("\n✅ Selected Columns:")
    print(df[cols].head())
    logging.info(f"Selected columns {cols} from {file_path}")

def save_output(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\n💾 Output saved to: {output_path}")
    logging.info(f"Saved output to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="🛠️ Automated CSV Processor CLI")
    parser.add_argument('--summarize', type=str, help='Summarize the given CSV file')
    parser.add_argument('--filter', nargs=3, metavar=('file', 'column', 'value'),
                        help='Filter rows in CSV file')
    parser.add_argument('--merge', nargs='+', help='Merge multiple CSV files')
    parser.add_argument('--select', nargs=2, metavar=('file', 'columns'),
                        help='Select specific columns (comma-separated)')
    parser.add_argument('--save', type=str, help='Output file path for saving result (used with --merge)')

    args = parser.parse_args()

    if args.summarize:
        if os.path.isfile(args.summarize):
            summarize_csv(args.summarize)
        else:
            print("❌ File not found.")

    elif args.filter:
        file, column, value = args.filter
        if os.path.isfile(file):
            filter_csv(file, column, value)
        else:
            print("❌ File not found.")

    elif args.merge:
        if all(Path(f).is_file() for f in args.merge):
            result = merge_csv(args.merge)
            if args.save:
                save_output(result, args.save)
        else:
            print("❌ One or more files are invalid.")

    elif args.select:
        file, columns = args.select
        if os.path.isfile(file):
            select_columns(file, columns)
        else:
            print("❌ File not found.")
    else:
        print("❗ Please provide at least one argument. Use --help for options.")

if __name__ == '__main__':
    main()
