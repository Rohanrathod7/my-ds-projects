# Automated CSV Processor CLI

Command-line tool to process CSVs:
- Summarize data
- Filter rows
- Merge files
- Select columns
- Save output

## Commands

```bash
python csv_processor.py --summarize sales1.csv
python csv_processor.py --filter sales2.csv Region East
python csv_processor.py --merge sales1.csv sales2.csv --save output.csv
python csv_processor.py --select sales1.csv Region,Sales
