import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from PIL import Image

st.set_page_config(
    page_title='ParagonCorp Products Sales Quantities Forecasting',
    layout = 'wide',
    initial_sidebar_state='expanded'
)

def run():
    # title
    st.title('Exploratory Data Analysis of the Dataset')
    st.write('by Ahmad Luay Adnani')


    # Add Image
    image = Image.open('paragon.png')
    st.image(image)

    # Description
    st.write('---')
    st.write('# Dataset') 
    st.write('Dataset provided by ParagonCorp.')

    # show dataframe
    df = pd.read_csv('sample_dataset_timeseries_noarea.csv')
    st.dataframe(df)

    ###
    # create a copy of the dataframe
    df_eda = df.copy()

    # EDA
    st.write('---')
    st.write('# Exploratory Data Analysis')
    select_eda = st.selectbox('Select EDA : ', ('Statistical Descriptive','Trend of Product Sales Quantities'))
    if select_eda == 'Statistical Descriptive':
        # measure of central tendency
        stats = df.describe().T
        st.dataframe(stats)
        st.write('Based on information above:')
        st.write("- The average product sales quantities is 3191.56.")
        st.write('- The range of product sales quantities is between  0 to 774,732.')

    else:
        # Trend of Product Sales Quantities
        # create a copy of the dataset
        df_eda = df.copy()

        # groupby week_end_date
        df_eda = df_eda.groupby("week_end_date")["quantity"].sum().to_frame().reset_index()

        # Set the date as index
        df_eda = df.set_index('week_end_date')

        # convert index to datetime
        df_eda.index = pd.to_datetime(df_eda.index)

        # drop columns
        df_eda.drop(columns=['week_number','week_start_date','product_item'],inplace=True)

        # convert index to datetime
        df_eda.index = pd.to_datetime(df_eda.index)

        # Select the proper time period for weekly aggregation
        df_eda = df_eda['2022-01-02':'2023-04-09'].resample('W').sum()
        
        # Trend
        # add linear line
        m, b = np.polyfit(range(len(df_eda)), df_eda['quantity'], 1)
        plt.figure(figsize=(10,4))
        plt.plot(df_eda.index, m*range(len(df_eda)) + b, label='Linear Trend Line',color='orange', alpha=0.6)

        # plot time series df_eda
        plt.plot(df_eda.index, df_eda['quantity'], marker = 'o', ms = 4, label='Product Sales Quantities')

        # add labels and legend
        plt.title('Trend of Product Sales Quantities')
        plt.xlabel('Date')
        plt.ylabel('quantity')
        plt.legend()

        # show plot
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        st.write('Here we can see the data of product sales quantities for the past 67 weeks. The trend is increasing over the past 67 weeks. There are no pattern on the products sales quantities. There are big spike that occur on 2022-05-08.')

if __name__ == '__main__':
    run()