import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, html, dcc

Ratings_chart = html.Div([
    html.Div('User Ratings Overview', 
             style={"textAlign": "left", 
                    'paddingLeft': '2vw', 
                    'paddingTop': '0.5vw', 
                    'paddingBottom': '0.5vw', 
                    'fontWeight': 'bold', 
                    "border": "0.1vw solid lightgrey", 
                    "border-top-left-radius": "0.8vw", 
                    "border-top-right-radius": "0.8vw", 
                    'fontSize': '1.2vw'}),
    
    dvc.Vega(id='rating_graph',
             spec={},
             style={"height": '24vh', 
                    "border": "0.1vw solid lightgrey", 
                    "border-bottom-left-radius": "0.8vw", 
                    "border-bottom-right-radius": "0.8vw", 'backgroundColor': 'white', 
                    'padding': '1.5vh', 
                    'paddingRight': '3vh',
                    'width': '36.85vw'})
    ], style={"marginTop": "1.5vh", 'width': '100%', 'height': '31vh'})


Purchase_history_chart = html.Div([
    html.Div(['User Purchase History'], 
             style={"textAlign": "left", 
                    'paddingLeft': '2vw', 
                    'paddingTop': '0.5vw', 
                    'paddingBottom': '0.5vw', 
                    'fontWeight': 'bold',"border": 
                    "0.1vw solid lightgrey", 
                    "border-top-left-radius": "0.8vw", 
                    "border-top-right-radius": "0.8vw", ''
                    'fontSize': '1.2vw'}),
    
    dvc.Vega(id='purchase_graph', 
                 spec={},
                 style={"height": '24vh', 
                        "border": "0.1vw solid lightgrey",
                        "border-bottom-left-radius": "0.8vw", 
                        "border-bottom-right-radius": "0.8vw", 'backgroundColor': 'white', 
                        'padding': '1.5vh', 
                        'paddingRight': '3vh',
                        'width': '36.85vw'})
    ], style = {'width': '100%', 'height': '31vh'})


Engagement_chart = html.Div([
    html.Div('User Engagement Levels', 
             style={"textAlign": "left", 
                    'paddingLeft': '2vw', 
                    'paddingTop': '0.5vw', 
                    'paddingBottom': '0.5vw', 
                    'fontWeight': 'bold', 
                    "border": "0.1vw solid lightgrey", 
                    "border-top-left-radius": "0.8vw", 
                    "border-top-right-radius": "0.8vw", 
                    'fontSize': '1.2vw'}),
    
    dvc.Vega(id='engagement_graph', 
                 spec={},
                 style={"height": '18vh', 
                        "border": "0.1vw solid lightgrey", 
                        "border-bottom-left-radius": "0.8vw", 
                        "border-bottom-right-radius": "0.8vw", 'backgroundColor': 'white', 
                        'padding': '1.5vh', 
                        'paddingRight': '3vh',
                        'width': '36.85vw'})
    ], style={'width': '100%', 'height': '26vh'})

