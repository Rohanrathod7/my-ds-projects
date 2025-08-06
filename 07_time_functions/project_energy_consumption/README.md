# 🔌 Energy Consumption Analyzer (Time-Series Analysis Project)

Analyze and visualize real-world appliance energy consumption data over time. This project applies time-series analysis techniques to extract insights from energy usage patterns within a smart home.

---

## 📦 Dataset

- **Name**: Appliances Energy Prediction  
- **Source**: UCI Machine Learning Repository  
- **Download**: [energydata_complete.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/00374/energydata_complete.csv)  
- **Kaggle Mirror**: [Kaggle Dataset](https://www.kaggle.com/datasets/loveall/appliances-energy-prediction)

The dataset contains over 19,000 records collected every 10 minutes, tracking:
- Appliance energy usage (Wh)
- Indoor & outdoor temperature and humidity
- Visibility, windspeed, pressure, weather, etc.

---

## 📘 Project Goals

- 🧹 Import and clean time-series data  
- ⏱ Extract time-based features (hour, day of week, etc.)  
- 📊 Visualize energy usage patterns over time  
- 🔗 Correlate environmental factors with energy consumption  
- 🔍 Identify behavioral usage patterns (spikes, efficiency gaps)

---

## 🛠 Key Features

### 🧼 Data Preparation
- Date parsing (`parse_dates`)
- Feature engineering (`hour`, `dayofweek`)
- Rolling window calculations

### 📈 Analysis & Visualization
- Average usage by hour and day
- Correlation heatmaps
- Distribution plots of usage
- Appliance usage during weekdays vs weekends

### 🔗 Advanced Reference
- Excellent article on time-series modeling:
  👉 [Time-Series Forecasting of Household Appliance Energy](https://dev.to/lucassul/time-series-forecasting-dha) by [@lucassul](https://dev.to/lucassul)

---

## 📊 Sample Output Visuals

- 📅 Line plot of average usage by hour
- 📊 Bar chart of usage by weekday
- 🧩 Heatmap of correlation between features (temperature, humidity, etc.)

---


---

## 💻 How to Run

1. Clone this repo or download the files  
2. Install required libraries (`pandas`, `matplotlib`, `seaborn`)  
3. Open `energy_analysis.ipynb` in Google Colab or Jupyter Notebook  
4. Run all cells to see results and visualizations  

---

## 🔍 Notable Kaggle Notebooks for Reference

- [Appliances Energy Prediction – MHassanz Aheer](https://www.kaggle.com/code/mhassanzaheer/appliances-energy-prediction-notebook)
- [EDA & Feature Trends – DeeDee NYC](https://www.kaggle.com/code/deedeenyc/appliances-energy-prediction)
- [Project 13 – Mohammed Mohsen](https://www.kaggle.com/code/mohammedmohsen0404/proj13-appliances-energy-prediction)
- [EDA & Feature Trends & Models Buillding – DeeDee NYC]([text](https://dev.to/lucassul/time-series-forecasting-dha))

---

## 📌 Possible Extensions

- 🔮 Forecast future energy consumption with ARIMA or Prophet
- 🧠 Predict energy usage using ML models
- 📈 Build dashboards using Streamlit or Dash

---

## 📎 License

This project is for educational and non-commercial use only. Dataset is from the UCI ML Repository and publicly available.

---