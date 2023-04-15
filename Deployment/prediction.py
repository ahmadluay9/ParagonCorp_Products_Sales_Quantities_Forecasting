import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load models 

with open('model_sarimax.pkl', 'rb') as file_1:
  model_sarimax = pickle.load(file_1)

def run():
  st.markdown("<h1 style='text-align: center;'>Products Sales Quantities Prediction</h1>", unsafe_allow_html=True)
  
  with st.form(key='Amazon_Customer_Review'):
            
      
      input = st.number_input('Title', min_value=0, max_value=99, value=5 ,step=1)
      submitted = st.form_submit_button('Predict')


  if submitted:
    
      # Predict
      result = model_sarimax.forecast(18).tail(input)
      result = pd.DataFrame(result)
      st.dataframe(result)

      # Forecast Visualization
      fig = plt.figure(figsize=(20,10))
      sns.lineplot(x=result.index, y=result.predicted_mean, data=result)
      plt.title(f'Prediction for the next {input} weeks', fontsize=20)
      plt.xlabel('Date', fontsize=16)
      plt.xticks(fontsize=8)
      plt.ylabel('Quantities Difference', fontsize=16)
      st.pyplot(fig)


if __name__ == '__main__':
    run()