import streamlit as st


def load_css():
    """
    Load custom dashboard CSS styles.
    """

    st.markdown(
        """
        <style>

        /* ==========================
           KPI CARDS
        ========================== */

        .metric-card {
            background: #1e293b;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.20);
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: 0px 8px 20px rgba(37,99,235,0.25);
        }

        /* ==========================
           INSIGHT BOXES
        ========================== */

        .insight-box {
            background: #16213e;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            border-left: 4px solid #2563eb;
        }

        /* ==========================
           TITLES
        ========================== */

        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
        }

        .sub-title {
            color: #cbd5e1;
            font-size: 1rem;
            margin-bottom: 1rem;
        }

        /* ==========================
           STREAMLIT METRICS
        ========================== */

        div[data-testid="metric-container"] {
            background: #1e293b;
            border: 1px solid #334155;
            padding: 12px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        }

        div[data-testid="metric-container"]:hover {
            border: 1px solid #2563eb;
        }

        /* ==========================
           SIDEBAR
        ========================== */

        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        /* ==========================
           DATAFRAME
        ========================== */

        div[data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }

        /* ==========================
           BUTTONS
        ========================== */

        .stButton > button {
            border-radius: 10px;
            border: none;
            background-color: #2563eb;
            color: white;
            font-weight: 600;
        }

        .stButton > button:hover {
            background-color: #1d4ed8;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
