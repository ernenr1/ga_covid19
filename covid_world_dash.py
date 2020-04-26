import numpy as np
import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

import requests

"""
Request world data
"""

url = "https://api.covid19api.com/summary"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data = payload)
world_data = response.json()

df_raw1 = pd.json_normalize(world_data["Countries"])

df_world=df_raw1.loc[0:246,['Country', 'CountryCode', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']]

df_world['TotalDeaths'] = df_world['TotalDeaths'].map(lambda x: "{:,}".format(x))
df_world['PositiveCases'] = df_world['TotalConfirmed'].map(lambda x: "{:,}".format(x))


df_world['text'] = "Country: "+df_world['CountryCode'].astype(str) +"<br>"+ "Positive Cases: "+df_world['PositiveCases'].astype(str) +"<br>"+ "Deaths: "+df_world['TotalDeaths'].astype(str)

world_fig = go.Figure(data=go.Choropleth(
    locations = df_world['Country'],
    z = df_world['TotalConfirmed'],
    text = df_world['text'],
    colorscale = 'Reds',
    locationmode = 'country names',
))

world_fig.update_layout(
    title_text='Test',
    geo=dict(
        #showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

"""
READ IN JSON data
From COVID19 API @
https://covidtracking.com/api/v1/states/current.json
"""

df_raw2 = pd.read_json('https://covidtracking.com/api/v1/states/current.json')

#Import data clean
df_us = df_raw2.loc[0:50, ['state', 'fips', 'positive', 'death']]

df_us['death'] = df_us['death'].map(lambda x: "{:,}".format(x))
df_us['positivecases'] = df_us['positive'].map(lambda x: "{:,}".format(x))

#Create new column in dataframe to include text
df_us['text'] = "State: "+df_us['state'].astype(str) +"<br>"+ "Positive Cases: "+df_us['positivecases'].astype(str) +"<br>"+ "Deaths: "+df_us['death'].astype(str)

#Create Plotly Choropleth

us_fig = go.Figure(data=go.Choropleth(
    locations=df_us['state'], # Spatial coordinates
    z = df_us['positive'], # Data to be color-coded
    text=df_us['text'],
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Positive Cases",
))

us_fig.update_layout(
    title_text = 'Positive COVID-19 Cases in the US',
    geo_scope='usa', # limit map scope to USA
)
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Hello World!'),
    dcc.Graph(figure=world_fig),
    dcc.Graph(figure=us_fig)
])
if __name__ == '__main__':
    app.run_server(debug=True)
