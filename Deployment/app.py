import streamlit as st
import eda # python file
import prediction # python file

navigation = st.sidebar.selectbox('Page Navigation: ',('Products Sales Quantities Prediction','EDA'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()

