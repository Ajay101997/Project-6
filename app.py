import streamlit as st
import pickle
import pandas as pd

# Load model
model=pickle.load(open("model.pkl","rb"))
st.title("Rossmann Sales Prediction app")
st.write("Enter store details to predict sales")

# User input
day_of_week=st.selectbox("Day of Week",[1,2,3,4,5,6,7])
promo=st.selectbox("Promo",[0,1])
school_holiday=st.selectbox("School Holiday",[0,1])
competition_distance=st.number_input("Competition Distance",min_value=0.0)
month=st.number_input("Month",1,12)
day=st.number_input("Day",1,31)
year=st.number_input("Year",2013,2015)

# Feature engineering
is_weekend=day_of_week in [6,7]
is_month_start=(day<=3)
is_month_end=(day>=28)

#Create input dataframe
inputDf=pd.DataFrame({"DayOfWeek":[day_of_week],"Open":[1],"Promo":[promo],"SchoolHoliday":[school_holiday],"CompetitionDistance":competition_distance,
                      "CompetitionOpenSinceMonth":[0],"CompetitionOpenSinceYear":[0],"Promo2":[0],"Promo2SinceWeek":[0],"Promo2SinceYear":[0],
                      "Year":[year],"Month":[month],"Day":[day],"IsWeekend":[is_weekend],"IsMonthStart":[is_month_start],"IsMonthEnd":[is_month_end]})

# Align features
train_columns=model.feature_names_in_
inputDf=inputDf.reindex(columns=train_columns,fill_value=0)

# Prediction
if st.button("Predict Sales"):
    prediction=model.predict(inputDf)
    st.success(f"Predicted Sales:{prediction[0]:.2f}")
