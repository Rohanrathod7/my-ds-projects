# 📊 A/B Testing on Web Conversion Data — Real-World Case Study

## 📝 Overview
This project performs **A/B testing** on a **real-world web conversion dataset** from an Udacity experiment.  
We compare the **control group (A)** and **treatment group (B)** to determine whether a **new landing page** leads to higher conversions.

We use:
- **Frequentist hypothesis testing** (two-proportion z-test)
- **Effect size calculation** (Cohen’s h)
- **Bayesian A/B testing**
- **Power analysis**
- **Sanity checks for randomization**
- **Business recommendation framework**

---

## 📂 Dataset
Source: [Udacity A/B Testing Data (Kaggle)](https://www.kaggle.com/datasets/zhangluyuan/ab-testing)  

**Columns:**
- `user_id` → Unique visitor ID
- `group` → `"control"` or `"treatment"`
- `landing_page` → `"old_page"` or `"new_page"`
- `converted` → `1` if user converted, else `0`

---

## 🎯 Business Context
A product team wants to test whether a new landing page increases conversion rates.  
Our goal:
- Test if **Treatment (B)** performs better than **Control (A)**
- Quantify the improvement and its practical significance
- Recommend whether to launch the new page

---

## 🧪 Hypothesis
**Null Hypothesis (H₀):** Conversion rate of A = Conversion rate of B  
**Alternative Hypothesis (H₁):** Conversion rate of B > Conversion rate of A  

Significance Level: **α = 0.05**

## 🔍 What the Code Does

1. **Data Loading & Cleaning**  
   - Load the dataset into a Pandas DataFrame  
   - Remove rows with mismatched `group` and `landing_page` assignments  
   - Drop duplicate user entries to ensure unbiased results  

2. **Sanity Checks**  
   - Confirm that the control group is served the old page and the treatment group is served the new page  
   - Verify balanced group sizes to validate randomization  

3. **Exploratory Data Analysis (EDA)**  
   - Calculate group-wise conversion rates  
   - Visualize conversion differences using bar plots  
   - Check for obvious trends or anomalies  

4. **Frequentist Hypothesis Testing**  
   - Perform a **two-proportion z-test** to compare conversion rates  
   - Calculate the p-value to determine statistical significance  

5. **Effect Size Measurement**  
   - Compute **Cohen’s h** to understand the magnitude of difference  
   - Classify the effect as small, medium, or large based on thresholds  

6. **Bayesian Analysis**  
   - Use a **Bayesian approach** to estimate the probability that the treatment conversion rate is higher than the control rate  
   - Generate posterior distributions for conversion rates  

7. **Power Analysis**  
   - Estimate the required sample size to detect a given minimum effect size with 80% power  

8. **Results Summary**  
   - Compile key metrics (conversion rates, p-value, effect size, Bayesian probability) into a summary table  
   - Provide a clear recommendation on whether to launch the new page  

---

## 📈 Key Output
- **Statistical conclusion**: Whether the difference is statistically significant  
- **Practical conclusion**: Whether the difference is large enough to matter in business terms  
- **Final recommendation**: Whether to implement the new landing page  

---

## 🚀 How to Run in Google Colab

2️⃣ Install dependencies:
```python
!pip install pandas numpy scipy matplotlib seaborn statsmodels pymc3 --quiet
