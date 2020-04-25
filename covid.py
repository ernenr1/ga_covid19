import numpy as np
import pandas as pd
import plotly.graph_objects as g


"""
READ IN JSON data
From COVID19 API @
https://covidtracking.com/api/v1/states/current.json
"""

dfimport = pd.read_json('https://covidtracking.com/api/v1/states/current.json')

#Import data clean
df = dfimport.loc[0:50, ['state', 'fips', 'positive', 'death']]
df['text'] = "State: "+df['state'].astype(str) +"<br>"+ "Positive Cases: "+df['positive'].astype(str) +"<br>"+ "Deaths: "+df['death'].astype(str)

fig = go.Figure(data=go.Choropleth(
    locations=df['state'], # Spatial coordinates
    z = df['positive'], # Data to be color-coded
    text=df['text'],
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Postive Cases",
))

fig.update_layout(
    title_text = 'Positive COVID-19 Cases in the US',
    geo_scope='usa', # limite map scope to USA
)

fig.write_html("/home/ernie/Documents/python/covid19/index.html")
