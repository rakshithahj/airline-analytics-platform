import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Airline Intelligence Platform",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# LOAD CUSTOM CSS
# -----------------------------
try:
    from utils.styles import load_css
    load_css()
except Exception as e:
    st.warning(f"Custom styles could not be loaded: {e}")

# -----------------------------
# MAIN PAGE
# -----------------------------
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

st.info("Use the sidebar to navigate between dashboard pages.")
