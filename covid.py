import numpy as np
import pandas as pd
import chart_studio.plotly as py
from plotly.offline import plot

"""
READ IN JSON data from COVID19
"""
dfimport = pd.read_json('https://covidtracking.com/api/v1/states/current.json')

#Import data clean
df = dfimport.loc[0:50, ['state', 'fips', 'positive', 'death']]


df['text'] = "State: "+df['state'].astype(str) +"<br>"+ "Positive Cases: "+df['positive'].astype(str) +"<br>"+ "Deaths: "+df['death'].astype(str)

data = [dict(type='choropleth', autocolorscale=True, locations=df['state'], z=df['positive'], locationmode='USA-states', text=df['text'], colorbar = dict(title="Postive Cases"))]

layout = dict(title='Positive COVID-19 Cases in the US', geo = dict(scope='usa', projection=dict(type='albers usa'), showlakes= True, lakecolor='rgb(66,165,245)',),)

fig = dict(data=data,layout=layout)

plot(fig, validate=False, filename='index.html')
