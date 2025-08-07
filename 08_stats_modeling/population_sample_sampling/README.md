# 📊 Population vs Sample Comparison using Bootstrapping (Advanced Analysis)

This mini-project explores **bootstrapping techniques** for comparing **population vs. sample statistics** using **real-world height data** from the NHANES (via `statsmodels`) survey dataset.

We demonstrate:
- The power of resampling
- Estimating sampling distribution of the mean
- Computing confidence intervals (percentile & basic)
- Bias and standard error of the estimator
- Comparison between bootstrap distribution and true sampling distribution

---

---

## 📈 Dataset

- **Source**: `survey` dataset from the `MASS` package (via `statsmodels`)
- **Field Used**: `Height` of **male respondents**
- **Preprocessing**:
  - Dropped `NaN` values
  - Filtered only `Sex == "Male"` for a homogeneous group

---

## 🎯 Objective

1. Estimate **mean height** from a sample.
2. Use **bootstrapping** to generate the **sampling distribution of the sample mean**.
3. Calculate:
   - Bootstrap **standard error**
   - Bootstrap **bias**
   - **95% Confidence Intervals** using:
     - Percentile method
     - Basic method
4. Visualize results and **compare**:
   - Sample mean
   - Bootstrap distribution
   - True population mean
   - True sampling distribution (optional)

---

## 🔍 Key Results (Sample Output)

| Metric                         | Value             |
|-------------------------------|-------------------|
| Population Mean               | 177.02 cm         |
| Sample Mean (n=50)           | 176.38 cm         |
| Bootstrap Mean               | 176.43 cm         |
| Bootstrap Std. Error         | 1.64              |
| Bootstrap Bias               | +0.05             |
| 95% CI (Percentile Method)   | [173.02, 179.75]  |
| 95% CI (Basic Method)        | [172.99, 179.73]  |

> 🚨 *These numbers may vary depending on the sample and bootstrap runs.*

