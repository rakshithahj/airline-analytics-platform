import streamlit as st
import plotly.express as px
import pandas as pd

from utils.loader import load_data

df = load_data()

st.title("👨‍👩‍👧 Passenger Analytics")

left,right = st.columns(2)

with left:

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
        title="Gender Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=[0,18,35,50,65,100],
        labels=[
            "0-18",
            "19-35",
            "36-50",
            "51-65",
            "65+"
        ]
    )

    fig = px.sunburst(
        df,
        path=[
            "Age Group",
            "Flight Status"
        ],
        title="Passenger Segmentation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

nationality = (
    df["Nationality"]
    .value_counts()
    .head(20)
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
    title="Top Nationalities"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
