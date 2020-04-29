import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime
import requests

#####################################################
"""
World Map Data/Plot
Using "COVID-19 API" @
https://covid19api.com/
"""
#####################################################

#####API Request#####
url = "https://api.covid19api.com/summary"
response = requests.get(url)
world_data = response.json()

#####Import raw JSON into Pandas Dataframe#####
df_raw1 = pd.json_normalize(world_data["Countries"])

#####Clean/Format Data for Plotly#####
df_world=df_raw1.loc[0:246,['Country', 'CountryCode', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered']]

df_world['TotalDeaths'] = df_world['TotalDeaths'].map(lambda x: "{:,}".format(x))
df_world['PositiveCases'] = df_world['TotalConfirmed'].map(lambda x: "{:,}".format(x))

#####Create new column within Dataframe to hold text strings for plot info#####
for col in df_world.columns:
    df_world[col] = df_world[col].astype(str)

df_world['text'] = "Country: "+df_world['CountryCode']+"<br>"+\
    "Positive Cases: "+df_world['PositiveCases']+"<br>"+\
    "Deaths: "+df_world['TotalDeaths']

#####Create choropleth plot/customize attributes#####
world_fig = go.Figure(data=go.Choropleth(
    locations = df_world['Country'],
    z = df_world['TotalConfirmed'],
    text = df_world['text'],
    colorscale = 'Reds',
    locationmode = 'country names',
    colorbar_title = "Positive Cases",
))

world_fig.update_layout(
    title_text='Positive COVID-19 Cases in the World',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

#####################################################
"""
US Map Data/Plot
Using "The COVID Tracking Project" API @
https://covidtracking.com/
"""
#####################################################

#####API request|Import raw JSON into Pandas Dataframe#####
df_raw2 = pd.read_json('https://covidtracking.com/api/v1/states/current.json')

#####Clean/Format Data for Plotly#####
df_us = df_raw2.loc[0:50, ['state', 'fips', 'positive', 'death']]

df_us['death'] = df_us['death'].map(lambda x: "{:,}".format(x))
df_us['positivecases'] = df_us['positive'].map(lambda x: "{:,}".format(x))

#####Create new column within Dataframe to hold text strings for plot info#####
for col in df_us.columns:
    df_us[col] = df_us[col].astype(str)

df_us['text'] = "State: "+df_us['state']+"<br>"+\
    "Positive Cases: "+df_us['positivecases']+"<br>"+\
    "Deaths: "+df_us['death']

#####Create choropleth plot/customize attributes#####
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

#####################################################
"""
DASH App intialization/Setup
"""
#####################################################

#####Date/Timestamp#####
curr=datetime.now()
dt_string = curr.strftime("%m/%d/%Y %H:%M:%S")

#####News headlines API request and stores in Pandas dataframe#####
def update_news():
    news_api = "http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=[KEY]"
    response_news = requests.get(news_api)
    news_data = response_news.json()
    df_news_import = pd.json_normalize(news_data["articles"])
    df_news = df_news_import.loc[0:20, ["title", "url"]]
    return df_news

#####HTML Object to display news headlines on app#####
def news_html_table(max_rows=20):
    df_news_html = update_news()
    return html.Div(
        [
            html.Div(
                html.Table(
                    #Header
                    [html.Tr([html.Th()])]
                    +
                    #body
                    [
                        html.Tr(
                            [
                                html.Td(
                                    html.A(
                                        df_news_html.iloc[i]["title"],
                                        href=df_news_html.iloc[i]["url"],
                                        target="_blank"
                                    )
                                )
                            ]
                        )
                        for i in range(min(len(df_news_html), max_rows))
                    ]
                ),
                style={"height": "750px", "overflowY": "scroll"},
            ),
        ],
        style={"height": "100%"}
    )

#####Reference Links for HTML/CSS Bootstrap#####
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
github = 'https://git.generalassemb.ly/Ernie-Enriquez/ga_covid19'
news_url = 'https://newsapi.org/'

#####DASH App server setup/HTML CSS Styling#####
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div(children=[
    html.H1(
        children='SARS-CoV-2 Map/News Tracker',
        style={
            'textAlign': 'center'
        }
    ),

    html.Div(html.H5(children='COVID-19 Statistics Dashboard (Hover map for more info)'), style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            # html.Div([
            #     dcc.Dropdown(
            #         options=[
            #             {'label': 'World Map', 'value': 'WM'},
            #             {'label': 'US Map', 'value': 'US'}
            #         ],
            #     placeholder='Select a Map',
            #     clearable=False,
            #     style=dict(width='50%')
            #     )
            # ]),
            html.Div([
                dcc.Graph(id='g1', figure=world_fig)
            ]),
            html.Div([
                dcc.Graph(id='g2', figure=us_fig),
            ],)
        ], className="eight columns", style={'width': '65%', 'display': 'inline-block'}),

        html.Div([
            html.H3("COVID News Live Feed"),
            news_html_table(),
            html.B(f"Map Data/News current as of: {dt_string}"),
            html.Br(),
            html.A('Code on Github', href=github),
            html.Br(),
            html.A('Powered by News API', href=news_url),
        ], className="four columns")
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
