import streamlit as st
from utils.styles import load_css

st.set_page_config(
    page_title="Airline Intelligence Platform",
    page_icon="✈️",
    layout="wide"
)

load_css()

st.title("✈️ Airline Intelligence Platform")

st.markdown("""
Welcome to the Airline Analytics Platform.

### Available Modules

- Executive Dashboard
- Passenger Analytics
- Geographical Analysis
- Pilot Performance
- AI Insights

Select a page from the left sidebar.
""")
