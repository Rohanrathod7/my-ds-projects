
# 🧠 HR Analytics Mini-Project

This project simulates real-world HR analytics using a synthetic employee dataset (`employees.csv`) generated with realistic data fields. The goal is to demonstrate both basic and advanced data analysis using Python and Pandas.

---

## 📊 Dataset Overview

| Column                  | Description                              |
|-------------------------|------------------------------------------|
| EmployeeID              | Unique ID for each employee              |
| Name                    | Full name (synthetic)                    |
| Department              | Department (Sales, R&D, IT, etc.)        |
| JobRole                 | Job title within department              |
| HireDate               | Date employee joined                     |
| MonthlyIncome           | Monthly salary                           |
| PerformanceRating       | Annual performance score (1 to 4)        |
| PercentSalaryHike       | Last salary hike percentage              |
| YearsAtCompany          | Derived from hire date                   |
| TrainingTimesLastYear   | Training sessions attended last year     |
| Attrition               | Whether the employee has left (Yes/No)   |

---

## 🔧 Tools Used

- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Faker** (for synthetic data generation)
- **Matplotlib / Seaborn** (for visualizations)

---

## 📈 Features & Operations Covered

This project demonstrates:

✅ Basic Operations:
- Reading/Writing CSV files  
- Subsetting & sorting  
- Adding new columns  

✅ Intermediate Analytics:
- Grouping & aggregation  
- Summary statistics  
- Indexing & slicing  
- Filtering with `.query()`  

✅ Advanced Operations:
- Merging datasets (inner, left, semi, anti joins)  
- `merge_asof` for time-based joins  
- `melt` for reshaping data  
- Forward-filling missing values  
- Validating merges with `validate=`  
- Advanced visualizations  

---

## 🚀 How to Use

1. Clone or download the project files.
2. Open `hr_analytics.ipynb` in Jupyter Notebook or Google Colab.
3. Upload and load `employees.csv`.
4. Run each cell to explore and analyze the data.

---

## 💡 Next Steps

You can extend the project by:

- Adding `performance_reviews.csv` (quarterly scores)
- Visualizing attrition vs salary or department
- Predicting attrition with machine learning

---

## 📌 License

This project uses synthetic data and is free to use for learning or demonstration purposes.

