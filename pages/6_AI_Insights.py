def generate_insights(df):

    insights = []

    delayed = (
        df["Flight Status"]
        .eq("Delayed")
        .mean()*100
    )

    insights.append(
        f"{delayed:.1f}% flights are delayed."
    )

    return insights
st.success(insight)
