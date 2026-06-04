pilot_stats = (
    df.groupby("Pilot Name")
      .agg({
          "Flight Status":"count"
      })
)
Pilot vs Flight Status Heatmap
df["Departure Date"] = pd.to_datetime(
    df["Departure Date"]
)
fig = px.line(
    monthly_data,
    x="Month",
    y="Flights"
)
