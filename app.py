import streamlit as st
import joblib 
import numpy as np

alcohol = joblib.load('alcohol.pkl')

st.title('Alcohol Price Prediction in Nepali Stores using Data Science and Machine Learning')

st.divider()

v = st.number_input('Enter Volume of Alcohol', min_value = 0, value=500)

a = st.number_input('Enter Percentage of Alcohol', min_value=5, value=40)

# c = st.number_input('Enter Category of Alcohol', min_value=0, max_value=8, value=5)
test = st.select_slider(label='Select Category of Alcohol by Sliding',options=['Beer','Brandy', 'Gin','Japanese Liquor', 'Liquor', 'Rum', 'Vodka', 'Whisky', 'Wine'],label_visibility='visible')

# st.selectbox(label='Select',options=['A','B','C','D'], )

if test == 'Beer':
    c = 0
elif test == 'Brandy':
    c = 1
elif test == 'Gin':
    c = 2
elif test == 'Japanese Liquor':
    c = 3
elif test == 'Liquor':
    c = 4
elif test == 'Rum':
    c = 5
elif test == 'Vodka':
    c = 6
elif test == 'Whisky':
    c = 7
elif test == 'Wine':
    c = 8

X = [[v,a,c]]
X_array = np.asarray(X)

st.divider()

btn = st.button('Predict Price')

if btn:
    prediction = alcohol.predict(X_array)
    result = (round(prediction[0],2)).astype(object)
    
    st.write(':green[The Price of Alcohol is Rs. ]',result)
    print(test)
    st.balloons()

st.divider()

st.write('Developed by SUSHAN BANIYA')

