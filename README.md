# Project-6
# 🏪 Sales Forecasting Across Multiple Retail Stores

## 📌 Project Overview

This project focuses on predicting daily sales of retail stores using Machine Learning and Deep Learning techniques.
It includes data preprocessing, exploratory data analysis (EDA), model building, evaluation, and deployment.

---

## 📊 Dataset

* Source: Rossmann Store Sales Dataset
* Includes store-level and time-based features
* Target Variable: **Sales**

---

## ⚙️ Data Preprocessing

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

## 📈 Exploratory Data Analysis (EDA)

### 🔹 Sales Distribution

* Sales data is right-skewed
* Outliers are present

👉 📌 Add your plot here:

```
Sales_Hostogram and Boxplot:

```
<img width="400" height="600" alt="Sales_histogram" src="https://github.com/user-attachments/assets/37d762e1-dfc4-432d-96e3-7cdbee798a81" />

<img width="400" height="600" alt="Sales_Boxplot" src="https://github.com/user-attachments/assets/1af23a64-d91e-4523-9d1a-c39a94882002" />


---

### 🔹 Log Transformation

* Applied `log1p` to reduce skewness
* Improved data distribution

👉 📌 Add plot:

```
![Log Sales](images/log_sales.png)
```

---

### 🔹 Bivariate Analysis

* Promotions increase sales
* Seasonal trends observed across months

👉 📌 Add plots:

```
![Month vs Sales](images/month_sales.png)
![Promo vs Sales](images/promo_sales.png)
```

---

### 🔹 Correlation Heatmap (if you created)

👉 📌 Add:

```
![Heatmap](images/heatmap.png)
```

---

## 🤖 Model Building

### 🔹 Random Forest

* Used pipeline with StandardScaler
* Achieved high accuracy

### 📊 Evaluation Metrics:

* R² Score ≈ High
* RMSE ≈ Low
* MAE ≈ Low

👉 📌 Add plot:

```
![Actual vs Predicted](images/rf_scatter.png)
```

---

### 🔹 LSTM Model

* Used for time-series prediction
* Captured trend but lower accuracy than RF

👉 📌 Add plot:

```
![LSTM Plot](images/lstm_plot.png)
```

---

## 📊 Example: Category Distribution (Percentage)

---

## 📌 Model Comparison

| Model         | Performance |
| ------------- | ----------- |
| Random Forest | ⭐ Best      |
| LSTM          | Moderate    |

---

## 🚀 Deployment

* Model deployed using **Streamlit**
* Allows real-time sales prediction

---

## 📌 Conclusion

* Random Forest performed best with high accuracy
* Sales influenced by promotions and seasonality
* LSTM captured trends but had higher errors
* End-to-end pipeline successfully implemented

---

## 🔮 Future Scope

* Improve LSTM with more features
* Use advanced models like GRU
* Deploy on cloud platforms
* Integrate real-time data

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* TensorFlow / Keras
* Streamlit

---

## 📌 Author

Your Name
