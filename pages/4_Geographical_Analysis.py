
fig = px.choropleth(
    nationality_counts,
    locations="Nationality",
    locationmode="country names",
    color="Passengers"
)
fig = px.treemap(
    continent_data,
    path=["Continents"],
    values="Passengers"
)
top_airports = (
    df.groupby("Airport Name")
      .size()
      .sort_values(ascending=False)
      .head(20)
)
Plotly Horizontal Bar
