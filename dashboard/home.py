import streamlit as st
import pandas as pd



st.title('COVID 19 ANALYSIS')

st.image(r"C:\Users\ritim\Downloads\covid19")

st.markdown('''COVID-19 data analysis involves examining the spread, impact, and trends of the pandemic using various data visualization techniques. 
By analyzing datasets containing information on confirmed cases, recoveries, deaths, and vaccination rates, we can uncover patterns in the virus’s transmission and its effects across different regions and time periods. ''')

df=pd.read_csv(r"C:\Users\ritim\OneDrive\Documents\Covid 19\covid_19_clean_complete.csv")

st.dataframe(df)

