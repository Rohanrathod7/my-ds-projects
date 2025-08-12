# Titanic Survival Prediction

This repository contains a Jupyter Notebook that demonstrates a step-by-step process for predicting survival on the Titanic using various machine learning models.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Data Analysis](#data-analysis)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Submission](#submission)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)

## Overview

This project aims to predict whether a passenger survived the Titanic shipwreck based on various features provided in the dataset. The notebook covers data loading, exploration, cleaning, feature engineering, training multiple machine learning models, evaluating their performance, and generating a submission file.

## Dataset

The dataset used in this project is the classic Titanic dataset, commonly found on platforms like Kaggle. It contains information about passengers, including their age, sex, class, fare, and survival status.

The data is loaded directly from GitHub:
- Training data: `https://raw.githubusercontent.com/Rohanrathod7/my-ds-projects/main/09_machine_learning/titanic_survival_prediction/Data/train.csv`
- Test data: `https://raw.githubusercontent.com/Rohanrathod7/my-ds-projects/main/09_machine_learning/titanic_survival_prediction/Data/test.csv`

## Data Analysis

The notebook includes initial data exploration to understand the dataset's structure, identify missing values, and analyze key features and their relationship with survival. This includes:

- Checking data types and non-null values (`.info()`)
- Generating summary statistics for numerical and categorical features (`.describe()`)
- Visualizing the distribution of features like Sex, Pclass, Embarked, Age, and Fare.
- Analyzing the survival rate across different categories.

## Feature Engineering

New features are created to potentially improve model performance:

- **Title**: Extracted from the 'Name' column and mapped to numerical values.
- **IsAlone**: Indicates whether a passenger is traveling alone based on 'SibSp' and 'Parch'.
- **IsMinor**: Indicates whether a passenger is under 15 years old.
- **Old_Female**: Indicates whether a passenger is an old female.
- Categorical features like 'Pclass', 'Sex', and 'Embarked' are converted into numerical format using one-hot encoding.
- Age and Fare are discretized into bands.

## Machine Learning Models

Several classification models are trained and evaluated using GridSearchCV for hyperparameter tuning and cross-validation:

- Logistic Regression
- Support Vector Classifier (SVC)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

The performance of each model is visualized using a bar plot showing their cross-validation scores.

## Results

The cross-validation scores for each model are displayed, and the best performing model (based on the highest cross-validation score) is identified.

## Submission

The best performing model is used to make predictions on the test dataset, and a submission file in the required format (PassengerId, Survived) is generated.

## Dependencies

The following libraries are required to run the notebook:

- pandas
- numpy
- matplotlib
- seaborn
- sklearn
- xgboost



## Summary:

### Data Analysis Key Findings

*   Six different machine learning models were trained and evaluated: Logistic Regression, SVC, Decision Tree, Random Forest, Gradient Boosting, and XGBoost.
*   GridSearchCV with 5-fold cross-validation was used to find the best hyperparameters for each model.
*   The best cross-validation scores obtained were: Logistic Regression: 80.70%, SVC: 82.83%, Decision Tree: 82.38%, Random Forest: 82.83%, Gradient Boosting: 82.26%, and XGBoost: 82.83%.
*   Multiple models (SVC, Random Forest, and XGBoost) achieved the highest best cross-validation score of 82.83%.
*   XGBoost was selected as the best performing model.
*   Predictions were made on the test dataset using the selected XGBoost model.
*   A submission file was generated with 'PassengerId' and 'Survived' columns.

### Insights or Next Steps

*   Since multiple models achieved the same highest score, further analysis or ensemble methods could be explored to potentially improve performance.
*   Consider analyzing the feature importances of the selected model (XGBoost) to gain insights into which features are most influential in predicting survival.
