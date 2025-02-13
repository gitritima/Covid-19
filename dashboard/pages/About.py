import streamlit as st
import pandas as pd

st.title("About Covid-19 Analysis")

df=pd.read_csv(r"C:\Users\ritim\OneDrive\Documents\Covid 19\covid_19_clean_complete.csv")

st.dataframe(df)

st.markdown('''This COVID-19 data analysis provides a detailed visualization of the pandemic's impact across different 
regions and time periods. Using interactive charts, it explores key trends such as the total number of confirmed cases, 
deaths, and recoveries worldwide. A line chart illustrates the progression of cases over time, highlighting significant 
spikes and trends in infections. A bar chart ranks the top 10 most affected countries, while a pie chart breaks down the 
distribution of confirmed, recovered, and fatal cases for a selected country. A scatter plot examines the relationship 
between confirmed cases and deaths, helping to identify fatality trends. Additionally, a heatmap visualizes the spread 
of COVID-19 across different time periods, and a global choropleth map provides a geographic representation of the 
outbreak’s severity in various countries. These visualizations offer valuable insights for health officials, researchers, 
and the public, 
helping to track the pandemic’s progression, assess policy effectiveness, and improve resource allocation.
''')