# ✈️ Flight Delay Analysis — Mini Project

Analyze and visualize flight delay patterns using a real-world small dataset. Explore key relationships between departure delays, airlines, airports, and time-based trends using Python.

---

## 📦 Dataset

- **Source**: [Flight Delay Sample Dataset on Kaggle](https://www.kaggle.com/datasets/izumita/flight-delay-sample)
- **Size**: Small, suitable for memory-efficient analysis (~few thousand rows)
- **Fields Include**:
  - `FL_DATE`: Flight date
  - `DEP_DELAY`: Departure delay (minutes)
  - `ARR_DELAY`: Arrival delay (minutes)
  - `ORIGIN`: Origin airport (IATA code)
  - `DEST`: Destination airport (IATA code)
  - `CARRIER`: Airline code
  - `DEP_TIME`: Actual departure time
  - `ARR_TIME`: Actual arrival time
  - `FL_NUM`: Flight number

---

## 🎯 Objective

This project aims to:

- Understand patterns in flight delays.
- Visualize delay distributions by time, carrier, and route.
- Derive insights to help optimize scheduling and resource allocation.
- Learn how datetime and timezone data affects operations.

---

## 🧰 Tools & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- (Optional) pytz / timezone-aware extensions

---

## 📊 Key Analyses Performed

### ✅ Time-based Analysis
- Delay trends across weekdays and months.
- Delay distribution by hour of the day.
- Flight volume trends over time.

### ✅ Airport & Route Performance
- Top delayed airports.
- Routes with highest average delays.
- Origin-destination pair analysis.

### ✅ Airline Insights
- Average delay by carrier.
- Carrier comparison visualizations.

### ✅ Correlation & Outliers
- Correlation between departure and arrival delays.
- Outlier detection in extreme delays.

---

## 🔎 Key Insights

- **Fridays** show the **highest average delays** across the board.
- **Morning flights** (6–9 AM) are more punctual than late afternoon flights.
- Certain **routes** (e.g., JFK to ORD) experience consistent delays.
- Some **airlines consistently outperform** others in on-time performance.
- Strong correlation found between `DEP_DELAY` and `ARR_DELAY`.

---

## 📂 Project Structure


---

## 🚀 How to Run

1. Clone or download this repository.
2. Download the dataset from Kaggle and place it in the root folder.
3. Run `flight_delay_analysis.ipynb` using:
   - [Google Colab](https://colab.research.google.com/)
   - Jupyter Notebook (Anaconda or VS Code)

---

## 🧠 Possible Extensions

- Timezone-aware scheduling and delay comparison using `tz_localize` and `tz_convert`.
- Flight duration modeling using scheduled vs actual timestamps.
- Dashboard development using Plotly/Dash or Streamlit.

---

## 📎 License

This project is for educational purposes and based on publicly available data.
