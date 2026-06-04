import streamlit as st
import pandas as pd
import plotly.express as px

from utils.loader import load_data
from utils.charts import (
    passenger_world_map,
    continent_treemap,
    top_airports_chart
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Geographical Analysis",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = load_data()

st.title("🌍 Geographical Analysis")
st.markdown(
    "Explore passenger distribution, countries, continents and airport activity worldwide."
)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("Filters")

selected_continent = st.sidebar.multiselect(
    "Select Continent",
    sorted(df["Continents"].dropna().unique()),
    default=sorted(df["Continents"].dropna().unique())
)

filtered_df = df[
    df["Continents"].isin(selected_continent)
]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_countries = filtered_df["Country Name"].nunique()
total_airports = filtered_df["Airport Name"].nunique()
total_continents = filtered_df["Continents"].nunique()

c1, c2, c3 = st.columns(3)

c1.metric("Countries", total_countries)
c2.metric("Airports", total_airports)
c3.metric("Continents", total_continents)

st.divider()

# ---------------------------------------------------
# WORLD MAP
# ---------------------------------------------------

st.subheader("🗺️ Global Passenger Distribution")

st.plotly_chart(
    passenger_world_map(filtered_df),
    use_container_width=True
)

# ---------------------------------------------------
# CONTINENT ANALYSIS
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🌎 Passenger Distribution by Continent")

    st.plotly_chart(
        continent_treemap(filtered_df),
        use_container_width=True
    )

with right:

    continent_data = (
        filtered_df["Continents"]
        .value_counts()
        .reset_index()
    )

    continent_data.columns = [
        "Continent",
        "Passengers"
    ]

    fig = px.bar(
        continent_data,
        x="Continent",
        y="Passengers",
        text_auto=True,
        title="Passenger Count by Continent"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# COUNTRY ANALYSIS
# ---------------------------------------------------

st.subheader("🏳️ Top Countries")

country_data = (
    filtered_df["Country Name"]
    .value_counts()
    .head(20)
    .reset_index()
)

country_data.columns = [
    "Country",
    "Passengers"
]

fig = px.bar(
    country_data,
    x="Passengers",
    y="Country",
    orientation="h",
    text_auto=True,
    title="Top 20 Countries by Passenger Volume"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# TOP AIRPORTS
# ---------------------------------------------------

st.subheader("✈️ Top Airports")

st.plotly_chart(
    top_airports_chart(filtered_df),
    use_container_width=True
)

# ---------------------------------------------------
# AIRPORT COUNTRY RELATIONSHIP
# ---------------------------------------------------

st.subheader("🌐 Airport Distribution by Country")

airport_country = (
    filtered_df.groupby("Country Name")
    ["Airport Name"]
    .nunique()
    .reset_index()
)

airport_country.columns = [
    "Country",
    "Airport Count"
]

fig = px.scatter(
    airport_country,
    x="Airport Count",
    y="Country",
    size="Airport Count",
    title="Countries vs Number of Airports"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# CONTINENT VS FLIGHT STATUS
# ---------------------------------------------------

st.subheader("📊 Flight Status by Continent")

heatmap_data = pd.crosstab(
    filtered_df["Continents"],
    filtered_df["Flight Status"]
)

fig = px.imshow(
    heatmap_data,
    text_auto=True,
    aspect="auto",
    title="Continent vs Flight Status"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------

with st.expander("View Geographic Dataset"):

    st.dataframe(
        filtered_df[
            [
                "Country Name",
                "Airport Name",
                "Continents",
                "Nationality",
                "Flight Status"
            ]
        ],
        use_container_width=True
    )

# ---------------------------------------------------
# INSIGHTS
# ---------------------------------------------------

st.subheader("🔍 Geographic Insights")

top_country = (
    filtered_df["Country Name"]
    .value_counts()
    .idxmax()
)

top_airport = (
    filtered_df["Airport Name"]
    .value_counts()
    .idxmax()
)

top_continent = (
    filtered_df["Continents"]
    .value_counts()
    .idxmax()
)

st.success(
    f"Highest passenger volume originates from: {top_country}"
)

st.success(
    f"Most active airport: {top_airport}"
)

st.success(
    f"Top performing continent by traffic: {top_continent}"
)
