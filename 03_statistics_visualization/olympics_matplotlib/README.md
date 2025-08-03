Olympic Games Data Analysis (1896–2016)
This project analyzes Olympic Games data (1896–2016) from the Kaggle dataset "120 years of Olympic history: athletes and results" using Python, Pandas, Matplotlib, and Seaborn. It provides advanced visualizations to explore medal trends, gender participation, and medal distribution across sports and countries, along with real-world insights into historical and socioeconomic factors.
Dataset

Source: Kaggle: 120 years of Olympic history
File: athlete_events.csv
Description: Contains ~270,000 rows of athlete event data from 1896 to 2016, including columns like Year, NOC (country code), Sport, Sex, and Medal.
Cleaning: The code removes rows with missing values for Medal, Year, Sex, Sport, and NOC and ensures appropriate data types.

Visualizations
The project generates three advanced Matplotlib visualizations:

Stacked Bar Chart: Medal counts (gold, silver, bronze) over time for a selected country (default: USA).
Line Plot: Trends in male and female athlete participation across Olympic years.
Heatmap: Medal distribution across sports for the top 10 countries by medal count.

Insights

Medal Trends: The USA dominates, often peaking in hosting years (e.g., 1996 Atlanta) due to home advantages like fan support.
Gender Participation: Female participation grew significantly, nearing parity by 2016, reflecting global gender equality efforts, though media coverage lags (4% for women vs. 40% participation).
Socioeconomic Factors: Wealthier nations (e.g., USA, Germany) lead due to sports infrastructure, but outliers like Australia show cultural emphasis.
Historical Context: Medal dips in the 1920s–1940s align with World Wars and the Great Depression. Boycotts (e.g., 1980, 1984) skewed results.
Sport-Specific: Athletics and Swimming dominate medals due to high event counts. Countries excel in culturally significant sports (e.g., China in Gymnastics).

Prerequisites

Google Colab: Run the code in a Colab notebook (https://colab.research.google.com/).
Kaggle API: Requires a Kaggle account and API key (kaggle.json).
Dependencies: Automatically installed via the script:
pandas
matplotlib
seaborn
kaggle



Setup and Running Instructions

Open Google Colab:

Create a new notebook at https://colab.research.google.com/.


Copy the Code:

Copy the Python script from the project code into a new code cell in your Colab notebook.


Obtain Kaggle API Key:

Go to your Kaggle account > Settings > API > Create New API Token.
Download kaggle.json.


Upload kaggle.json:

Run the code in Colab. When prompted, click "Choose Files" and upload kaggle.json.
Alternatively, manually upload athlete_events.csv to Colab and modify the code to read it directly (e.g., df = pd.read_csv('/content/athlete_events.csv')).


Run the Code:

Execute the code cell. It will:
Install dependencies (pandas, matplotlib, seaborn, kaggle).
Download and unzip the Kaggle dataset.
Generate three visualizations and print insights.




View Outputs:

Stacked Bar Chart: Shows medal counts for the USA by year.
Line Plot: Displays male and female participation trends.
Heatmap: Shows medal distribution for top 10 countries across sports.
Insights: Printed below the visualizations with analysis.



Customization

Change Country: Modify the country parameter in plot_medal_trends (e.g., country='CHN') to analyze another country.
Adjust Heatmap: Change top_n_countries in plot_medal_heatmap (e.g., top_n_countries=5) for fewer or more countries.
Local Execution: To run locally, install dependencies (pip install pandas matplotlib seaborn) and use the dataset directly.

Notes

Performance: The dataset (~270,000 rows) is manageable in Colab, but the heatmap may take a moment to render for large datasets.
Dataset Access: Ensure your Kaggle API key is valid to download the dataset automatically.
Visualization Style: Uses the seaborn Matplotlib style for enhanced aesthetics, with custom colors for medals (gold: #FFD700, silver: #C0C0C0, bronze: #CD7F32).

License
This project uses the Kaggle dataset under its respective license. Ensure compliance with Kaggle's terms for dataset usage.