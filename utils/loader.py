import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Airline Dataset Updated - v2.csv"
    )

    df["Departure Date"] = pd.to_datetime(
        df["Departure Date"],
        errors="coerce"
    )

    return df
