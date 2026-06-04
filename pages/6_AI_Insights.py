import streamlit as st

from utils.loader import load_data

df = load_data()

st.title("🤖 AI Insights")

top_country = (
    df["Country Name"]
    .value_counts()
    .idxmax()
)

top_airport = (
    df["Airport Name"]
    .value_counts()
    .idxmax()
)

top_pilot = (
    df["Pilot Name"]
    .value_counts()
    .idxmax()
)

avg_age = round(
    df["Age"].mean(),
    1
)

delay_pct = round(
    (
        df["Flight Status"]
        .eq("Delayed")
        .mean()
    ) * 100,
    2
)

st.success(
    f"Most passengers originate from {top_country}"
)

st.success(
    f"Highest traffic airport: {top_airport}"
)

st.success(
    f"Most active pilot: {top_pilot}"
)

st.success(
    f"Average passenger age is {avg_age}"
)

st.success(
    f"Delay rate is {delay_pct}%"
)

st.info("""
### Key Findings

• Passenger traffic is concentrated around a few major airports.

• Most travelers belong to the 19-50 age segment.

• Flight operations are largely stable.

• A small set of pilots operate the majority of flights.

• Geographic distribution is globally diversified.
""")
