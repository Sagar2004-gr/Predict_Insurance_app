import streamlit as st
import pickle
import pandas as pd
import numpy as np

# load model
model = pickle.load(open('gb_model.pkl','rb'))

st.title('Insurance Price Prediction App')

# inputs
age = st.number_input('Age',min_value=1, max_value=100,value=25)
gender = st.selectbox('Gender',('male','female'))
bmi = st.number_input('BMI',min_value=10.0, max_value=80.0,value=30.0)
smoker = st.selectbox('Smoker',('yes','no'))
children = st.number_input('Children',min_value=0, max_value=10,value=2)
region = st.selectbox('Region',('southwest','southeast','northwest','northeast'))

# encoding
smoker = 1 if smoker=='yes' else 0
sex_male = 1 if gender=='male' else 0
sex_female = 1 if gender=='female' else 0

region_dict = {'southeast':3,'northeast':2,'northwest':1,'southwest':0}
Region = region_dict[region]

# dataframe
input_features = pd.DataFrame({
    'age':[age],
    'bmi':[bmi],
    'children':[children],
    'Smoker':[smoker],
    'sex_female':[sex_female],
    'sex_male':[sex_male],
    'Region':[Region]
})

# prediction
if st.button('Predict'):
    prediction = model.predict(input_features)
    output = round(np.exp(prediction[0]),2)
    st.success(f'Price Prediction: ${output}')
