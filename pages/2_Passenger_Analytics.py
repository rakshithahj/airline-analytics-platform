fig = px.histogram(
    df,
    x="Age",
    nbins=25,
    marginal="box"
)
fig = px.sunburst(
    df,
    path=["Gender","Flight Status"]
)
0-18
19-35
36-50
51-65
65+
Age Group × Flight Status
