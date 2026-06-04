import pandas as pd
import streamlit as st
from pathlib import Path


@st.cache_data
def load_data():
    """
    Load airline dataset safely.
    """

    # Dataset location
    file_path = Path("data") / "Airline Dataset Updated - v2.csv"

    # Verify file exists
    if not file_path.exists():
        st.error(
            f"Dataset file not found:\n{file_path}\n\n"
            "Make sure the CSV exists inside the data folder "
            "and is committed to GitHub."
        )
        st.stop()

    # Read dataset
    df = pd.read_csv(file_path)

    # Convert date column
    if "Departure Date" in df.columns:
        df["Departure Date"] = pd.to_datetime(
            df["Departure Date"],
            errors="coerce"
        )

    return df
