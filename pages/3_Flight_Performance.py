import streamlit as st
import plotly.express as px

from utils.loader import load_data

df = load_data()

st.title("🌍 Geographical Analysis")

country_counts = (
    df.groupby("Country Name")
    .size()
    .reset_index(name="Passengers")
)

fig = px.choropleth(
    country_counts,
    locations="Country Name",
    locationmode="country names",
    color="Passengers",
    title="Passenger Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

continent = (
    df["Continents"]
    .value_counts()
    .reset_index()
)

continent.columns = [
    "Continent",
    "Passengers"
]

fig = px.treemap(
    continent,
    path=["Continent"],
    values="Passengers",
    title="Passengers by Continent"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

airport = (
    df["Airport Name"]
    .value_counts()
    .head(15)
    .reset_index()
)

airport.columns = [
    "Airport",
    "Flights"
]

fig = px.bar(
    airport,
    x="Flights",
    y="Airport",
    orientation="h",
    title="Top Airports"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
