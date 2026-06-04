import pandas as pd

def get_kpis(df):

    return {

        "Passengers": len(df),

        "Airports":
        df["Airport Name"].nunique(),

        "Countries":
        df["Country Name"].nunique(),

        "Pilots":
        df["Pilot Name"].nunique(),

        "Average Age":
        round(df["Age"].mean(), 1)
    }


def top_airports(df, n=10):

    return (
        df["Airport Name"]
        .value_counts()
        .head(n)
        .reset_index()
    )


def top_pilots(df, n=10):

    return (
        df["Pilot Name"]
        .value_counts()
        .head(n)
        .reset_index()
    )
