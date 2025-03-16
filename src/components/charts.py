import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, html, dcc

Ratings_chart = dbc.Card(
    [dbc.CardHeader('User Ratings Overview',
                    style={"textAlign": "left",
                           'paddingLeft': '2vw',
                           'fontWeight': 'bold'}),
     dbc.CardBody([html.Div(dvc.Vega(id='rating_graph', spec={}, style={"height": '20vh'}))])],
     style={'width': '100%','height': '29vh', 'marginTop': '2vh'})

Purchase_history_chart = dbc.Card(
    [dbc.CardHeader('User Purchase History',
                    style={"textAlign": "left",
                          'paddingLeft': '2vw', 
                          'fontWeight': 'bold'}),
     dbc.CardBody([html.Div(dvc.Vega(id='purchase_graph', spec={}, style={"height": '20vh'}))])],
     style={"marginTop": "1.5vh", 'width': '100%', 'height': '29vh'})

Engagement_chart = dbc.Card(
    [dbc.CardHeader('User Engagement Levels',
                    style={"textAlign": "left",
                           'fontWeight': 'bold'}),
     dbc.CardBody([html.Div(dvc.Vega(id='engagement_graph', spec={}, style={"height": '15vh'}))])],
    style={"marginTop": "1.5vh", 'width': '100%', 'height': '24vh'})
