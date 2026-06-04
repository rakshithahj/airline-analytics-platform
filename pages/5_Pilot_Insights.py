import streamlit as st
import plotly.express as px
import pandas as pd

from utils.loader import load_data

df = load_data()

st.title("🧑‍✈️ Pilot Performance")

pilot = (
    df["Pilot Name"]
    .value_counts()
    .head(20)
    .reset_index()
)

pilot.columns = [
    "Pilot",
    "Flights"
]

fig = px.bar(
    pilot,
    x="Flights",
    y="Pilot",
    orientation="h",
    title="Top Pilots"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

heat = pd.crosstab(
    df["Pilot Name"],
    df["Flight Status"]
)

heat = heat.head(20)

fig = px.imshow(
    heat,
    text_auto=True,
    title="Pilot Status Matrix"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
