import streamlit as st
import plotly.express as px

from utils.loader import load_data
from utils.analytics import get_kpis

df = load_data()

st.title("📊 Executive Dashboard")

kpis = get_kpis(df)

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Passengers", f"{kpis['Passengers']:,}")
c2.metric("Airports", kpis["Airports"])
c3.metric("Countries", kpis["Countries"])
c4.metric("Pilots", kpis["Pilots"])
c5.metric("Avg Age", kpis["Average Age"])

st.divider()

left,right = st.columns(2)

with left:

    fig = px.pie(
        df,
        names="Flight Status",
        hole=.6,
        title="Flight Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(
        df,
        x="Age",
        nbins=30,
        title="Age Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

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

st.plotly_chart(
    fig,
    use_container_width=True
)
