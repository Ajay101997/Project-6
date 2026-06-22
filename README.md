# Project-6
# Sales Forecasting Across Multiple Retail Stores

## Project Overview

This project focuses on predicting daily sales of retail stores using Machine Learning and Deep Learning techniques.
It includes data preprocessing, exploratory data analysis (EDA), model building, evaluation, and deployment.

---

## Dataset

* Source: Rossmann Store Sales Dataset
* Includes store-level and time-based features
* Target Variable: **Sales**

---

## Data Preprocessing

* Merged train and store datasets using `Store` column
* Handled missing values using median and default values
* Converted `Date` into datetime format
* Extracted features: Year, Month, Day
* Created new features:

  * IsWeekend
  * IsMonthStart
  * IsMonthEnd
* Dropped unnecessary columns like `Store`, `Date`, and `Customers` (to avoid data leakage)

---

## Exploratory Data Analysis (EDA)

### Sales Distribution

* Sales data is right-skewed
* Outliers are present

Add your plot here:

```
Sales_Hostogram & Sales_Boxplot:

```
<img width="700" height="400" alt="Sales_histogram" src="https://github.com/user-attachments/assets/37d762e1-dfc4-432d-96e3-7cdbee798a81" />
<img width="700" height="400" alt="Sales_Boxplot" src="https://github.com/user-attachments/assets/1af23a64-d91e-4523-9d1a-c39a94882002" />

---

### Log Transformation

* Applied `log1p` to reduce skewness
* Improved data distribution

Add plot:

```
Log Sales:
```
<img width="700" height="400" alt="LogTransformed_Sales" src="https://github.com/user-attachments/assets/34ea692d-1dab-4fb4-874f-f64e1fbc2f71" />

---

### Bivariate Analysis

* Promotions increase sales
* Seasonal trends observed across months

Add plots:

```
Month vs Sales & Promo vs Sales:
```
<img width="700" height="400" alt="Month Vs Sales" src="https://github.com/user-attachments/assets/466b89b0-e9dc-44a1-9f06-c55b8f53d9ec" />
<img width="700" height="400" alt="Promo Vs Sales" src="https://github.com/user-attachments/assets/8e411e1b-4253-4b6d-8e91-e11f78775713" />

---

### Correlation Heatmap (if you created)

Add:

```
Correlation_Heatmap:
```
<img width="800" height="500" alt="Correlation_Heatmap" src="https://github.com/user-attachments/assets/f97db8c4-51c3-4c46-9186-827f667c9771" />

---

## Model Building

### Random Forest

* Used pipeline with StandardScaler
* Achieved high accuracy

### Evaluation Metrics:

* MSE: 763173.4463319121
* RMSE: 873.5979889697046
* MAE: 503.365833791695
* R2 Score: 0.948371888422028

Add plot:

```
Actual vs Predicted:
```
<img width="700" height="400" alt="Actual Vs Predicted" src="https://github.com/user-attachments/assets/d22077bb-bc91-491f-aa8d-362778e86d78" />

---

### LSTM Model

* Used for time-series prediction
* Captured trend but lower accuracy than RF

Add plot:

```
LSTM Prediction vs Actual:
```
<img width="700" height="400" alt="LSTM_Sales" src="https://github.com/user-attachments/assets/90bce5b3-aa4a-49d4-a24e-b57b875f2bda" />
<img width="700" height="400" alt="LSTM_Actual Vs Predicted" src="https://github.com/user-attachments/assets/42495509-2d9c-401f-9e5b-dfa887f0dea1" />

---


## Model Comparison

| Model         | Performance |
| ------------- | ----------- |
| Random Forest | Best        |
| LSTM          | Moderate    |

---

## Deployment

* Model deployed using **Streamlit**
* Allows real-time sales prediction
```

Rossmann Sales Prediction App:
```
<img width="700" height="400" alt="Streamlit" src="https://github.com/user-attachments/assets/2d7469de-d232-475f-9f7f-9173bbf222c4" />


## Conclusion

* Random Forest performed best with high accuracy
* Sales influenced by promotions and seasonality
* LSTM captured trends but had higher errors
* End-to-end pipeline successfully implemented

---

## Future Scope

* Improve LSTM with more features
* Use advanced models like GRU
* Deploy on cloud platforms
* Integrate real-time data

---

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* TensorFlow / Keras
* Streamlit

---

## Author

Mr. Ajay Kumar Sahu
