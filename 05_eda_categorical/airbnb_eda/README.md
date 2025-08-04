# Airbnb NYC Listings — Comprehensive EDA

## 📌 Goal
Explore patterns in Airbnb listings in NYC focusing on price behavior, neighborhood differences, room types, and review activity.

## 📊 Dataset
~49,000 listings with metadata like price, location, reviews, and availability.

## 🔎 Analysis Highlights
- Cleaning & validation of price and review data  
- Missing value strategy for `reviews_per_month` and `last_review`  
- Handling outliers in price  
- Categorical distributions (`room_type`, `neighborhood_group`)  
- Cross-tabs and correlation analysis  
- Data transformation using `pd.cut()`  
- Trend analysis over time (`last_review` month)  
- Hypothesis testing (Manhattan price premium)

## 🧠 Insights Generated
- Entire homes cost ~2× more than private rooms  
- Listings in Manhattan cost ~30% more than other boroughs  
- Neighborhoods with high counts and similar listing types (e.g. Brooklyn + Private Room)  
- Seasonal effects visible in review activity
