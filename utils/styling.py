import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .metric-card{
        background:#1e293b;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.2);
    }

    .insight-box{
        background:#16213e;
        padding:15px;
        border-radius:12px;
        margin-bottom:10px;
    }

    </style>
    """,
    unsafe_allow_html=True)
