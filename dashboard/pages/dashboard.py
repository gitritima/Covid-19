import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():

    df=pd.read_csv(r"C:\Users\ritim\OneDrive\Documents\Covid 19\covid_19_clean_complete.csv")
    return df

df=load_data()



latest_df = df.groupby("Country/Region")["Confirmed"].max().reset_index()

# Choropleth Map
st.title(" Global COVID-19 Cases")
fig = px.choropleth(latest_df, locations="Country/Region", locationmode="country names",
                    color="Confirmed", title="Global COVID-19 Spread",
                    color_continuous_scale="Reds")
st.plotly_chart(fig)

st.markdown("Key Insights : ")
st.markdown('1. This graph shows the impact of covid 19 cases all over the world.')
st.markdown("2. The more red the area is , the greater the impact of covid 19 cases is.")




country_cases = df.groupby("Country/Region")["Confirmed"].max().reset_index()
top_countries = country_cases.sort_values(by="Confirmed", ascending=False).head(10)

# Plot bar chart
st.title(" Top 10 Countries by COVID-19 Cases")
fig = px.bar(top_countries, x="Country/Region", y="Confirmed", 
             title="Top 10 Countries with Most Cases", color="Confirmed")
st.plotly_chart(fig)

st.markdown("Key Insights : ")
st.markdown("1. The country with the most cases is - United States")
st.markdown("2. The country with the least cases is  - Iran")


country_cases = df.groupby("Country/Region")["Deaths"].max().reset_index()
top_countries = country_cases.sort_values(by="Deaths", ascending=False).head(10)

# Plot bar chart
st.title(" Top 10 Countries by Deaths due to COVID-19 Cases")
fig = px.bar(top_countries, x="Country/Region", 
             y="Deaths", 
             title="Top 10 Countries with Most Deaths", 
             color="Deaths",
             color_continuous_scale='sunsetdark')
st.plotly_chart(fig)

st.markdown('Key Insights : ')
st.markdown('1. The country with the most deaths is - United States')
st.markdown("2. The country with the least deaths is - Iran")


country_cases = df.groupby("Country/Region")["Active"].max().reset_index()
top_countries = country_cases.sort_values(by="Active", ascending=False).head(10)

# Plot bar chart
st.title(" Top 10 Countries With Active COVID-19 Cases")
fig = px.bar(top_countries, x="Country/Region", 
             y="Active", 
             title="Top 10 Countries with Most Active Cases", 
             color="Active",
             color_continuous_scale='sunset')
st.plotly_chart(fig)

st.markdown('Key Insights :')
st.markdown('1. The country with the most active cases is - United States')
st.markdown("2. The country with the least active cases is - Italy")



st.title(" COVID-19 Cases vs. Deaths")
fig = px.scatter(df, x="Confirmed", y="Deaths", color="Country/Region",
                 title="Relationship Between Confirmed Cases and Deaths")
st.plotly_chart(fig)

st.markdown('Key Insights :')

st.markdown('1. Linear Trend (Proportional Increase in Deaths with Cases)')

st.markdown('2. Indicates a consistent mortality rate across countries.')

st.markdown('3. The trend shows how deaths increase with rising confirmed cases')




st.sidebar.header("Filters")
countries = df["Country/Region"].unique()
selected_country = st.sidebar.selectbox("Select a Country", countries)

# Filter data for selected country
filtered_df = df[df["Country/Region"] == selected_country]

# Line chart visualization
st.title(f" COVID-19 Trends in {selected_country}")

fig = px.line(
    filtered_df,
    x="Date",
    y=["Confirmed", "Deaths", "Recovered","Active"],
    title=f"COVID-19 Cases in {selected_country}",
    labels={"value": "Count", "Date": "Date"},
    template="plotly_dark"
)

st.plotly_chart(fig)

st.markdown("Key Insights :")
st.markdown('1. Steep Upward Slope (Rapid Increase in Cases) → Indicates outbreak waves or sudden surges in infections.')
st.markdown('2. Plateau (Flattening of the Curve) → Suggests containment or declining infection rates.')
st.markdown('3. Recovery Rate Trends → If the Recovered line is close to the Confirmed Cases line, it suggests a high recovery rate.')
st.markdown('4. Death Rate Trends → If the Deaths line rises significantly without a matching increase in recoveries, it may indicate a severe outbreak or strain on healthcare.')
st.markdown('5. Active Cases Decline → Indicates successful control measures, vaccination, or natural immunity development.')



country_df = df[df["Country/Region"] == selected_country].iloc[-1]

# Pie chart data
values = [country_df["Deaths"], country_df["Recovered"],country_df['Active']]
labels = ["Deaths", "Recovered","Active"]

# Create pie chart
st.title(f" COVID-19 Case Distribution in {selected_country}")
fig = px.pie(names=labels, values=values, title=f"COVID-19 Case Breakdown - {selected_country}")

fig.update_traces(marker=dict(colors=["#FFA500", "#228B22", "#DC143C"]))


st.plotly_chart(fig)


st.markdown("Key Insights :")

st.markdown('1. Higher Recovery Percentage → Indicates effective treatment and containment.')
st.markdown('2. High Active Cases → Suggests ongoing transmission and new infections.')
st.markdown('3. High Death Proportion → Indicates poor healthcare infrastructure or late interventions.')
st.markdown('4. Balanced Distribution → Suggests a well-managed outbreak with recoveries increasing alongside.')






pivot_df = df.pivot_table(index="Date", columns="Country/Region", values="Confirmed", aggfunc="sum")

# Heatmap
st.title("COVID-19 Heatmap Over Time")
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot_df.fillna(0), cmap="RdYlBu", ax=ax)
st.pyplot(fig)


st.markdown('Key Insights :')
st.markdown('1. Darker Colors = More Cases → Indicates high case surges (peaks in transmission).')
st.markdown('2. Lighter Colors = Fewer Cases → Suggests effective control or early outbreak stage.')
st.markdown('3. Clusters of High Cases → Reveal waves or spikes of infection (e.g., lockdown periods, new variants).')
st.markdown('4. Comparing Countries → Helps identify which regions had more severe outbreaks at different times.')