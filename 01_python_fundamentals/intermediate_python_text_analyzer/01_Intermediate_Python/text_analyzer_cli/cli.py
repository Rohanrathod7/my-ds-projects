import argparse
from analyzer import TextAnalyzer
from utils import load_text_file

def main():
    parser = argparse.ArgumentParser(description="Text Analyzer Tool")
    parser.add_argument("file", help="Path to the text file to analyze")
    file = parser.parse_args()

    text = load_text_file(file.file)
    analyzer = TextAnalyzer(text)

    for(key, value) in analyzer.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    main()