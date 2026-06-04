
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
