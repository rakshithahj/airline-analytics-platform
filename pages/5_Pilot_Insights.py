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
delay_rate_by_country
delay_rate_by_airportAge
Gender
Country
Flight Status
delay_rate_by_continent
