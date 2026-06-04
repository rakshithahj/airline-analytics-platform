
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# =====================================================
# FLIGHT STATUS DONUT
# =====================================================

def flight_status_donut(df):

    fig = px.pie(
        df,
        names="Flight Status",
        hole=0.65,
        title="Flight Status Distribution"
    )

    fig.update_layout(
        height=500,
        legend_title="Status"
    )

    return fig


# =====================================================
# AGE DISTRIBUTION
# =====================================================

def age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=30,
        marginal="box",
        title="Passenger Age Distribution"
    )

    fig.update_layout(
        height=500
    )

    return fig


# =====================================================
# GENDER DISTRIBUTION
# =====================================================

def gender_distribution(df):

    gender = (
        df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = [
        "Gender",
        "Count"
    ]

    fig = px.bar(
        gender,
        x="Gender",
        y="Count",
        title="Gender Distribution",
        text_auto=True
    )

    return fig


# =====================================================
# CONTINENT TREEMAP
# =====================================================

def continent_treemap(df):

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
        title="Passenger Distribution by Continent"
    )

    return fig


# =====================================================
# TOP AIRPORTS
# =====================================================

def top_airports_chart(df, top_n=15):

    airport = (
        df["Airport Name"]
        .value_counts()
        .head(top_n)
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
        title=f"Top {top_n} Airports",
        text_auto=True
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    return fig


# =====================================================
# TOP NATIONALITIES
# =====================================================

def nationality_chart(df, top_n=20):

    nationality = (
        df["Nationality"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    nationality.columns = [
        "Nationality",
        "Passengers"
    ]

    fig = px.bar(
        nationality,
        x="Nationality",
        y="Passengers",
        title=f"Top {top_n} Nationalities"
    )

    return fig


# =====================================================
# MONTHLY TREND
# =====================================================

def monthly_trend(df):

    monthly = (
        df
        .set_index("Departure Date")
        .resample("M")
        .size()
        .reset_index(name="Flights")
    )

    fig = px.line(
        monthly,
        x="Departure Date",
        y="Flights",
        markers=True,
        title="Monthly Flight Trend"
    )

    return fig


# =====================================================
# WORLD MAP
# =====================================================

def passenger_world_map(df):

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
        hover_name="Country Name",
        title="Global Passenger Distribution"
    )

    return fig


# =====================================================
# TOP PILOTS
# =====================================================

def top_pilots_chart(df, top_n=20):

    pilot = (
        df["Pilot Name"]
        .value_counts()
        .head(top_n)
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
        title=f"Top {top_n} Pilots",
        text_auto=True
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    return fig


# =====================================================
# PILOT HEATMAP
# =====================================================

def pilot_status_heatmap(df):

    heat = pd.crosstab(
        df["Pilot Name"],
        df["Flight Status"]
    )

    heat = heat.head(20)

    fig = px.imshow(
        heat,
        text_auto=True,
        aspect="auto",
        title="Pilot Performance Matrix"
    )

    return fig


# =====================================================
# CONTINENT VS FLIGHT STATUS
# =====================================================

def continent_status_heatmap(df):

    heat = pd.crosstab(
        df["Continents"],
        df["Flight Status"]
    )

    fig = px.imshow(
        heat,
        text_auto=True,
        aspect="auto",
        title="Continent vs Flight Status"
    )

    return fig


# =====================================================
# AGE GROUP SUNBURST
# =====================================================

def passenger_segmentation(df):

    temp = df.copy()

    temp["Age Group"] = pd.cut(
        temp["Age"],
        bins=[0, 18, 35, 50, 65, 100],
        labels=[
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "65+"
        ]
    )

    fig = px.sunburst(
        temp,
        path=[
            "Age Group",
            "Gender",
            "Flight Status"
        ],
        title="Passenger Segmentation"
    )

    return fig


# =====================================================
# KPI GAUGE
# =====================================================

def ontime_gauge(df):

    ontime = (
        df["Flight Status"]
        .eq("On Time")
        .mean()
    ) * 100

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ontime,
            title={"text": "On-Time Performance"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    fig.update_layout(
        height=350
    )

    return fig
