import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, html, dcc

Ratings_chart = html.Div([
    html.Div('User Ratings Overview', style={"textAlign": "left", 'paddingLeft': '2vw', 'paddingTop': '0.5vw', 'paddingBottom': '0.5vw', 'fontWeight': 'bold', "border": "1px solid lightgrey", "border-top-left-radius": "8px", "border-top-right-radius": "8px", 'fontSize': '16px', 'marginLeft': '0.75vw', 'marginRight': '0.75vw'}),
    
    html.Div(
        [dbc.Container([html.Div(dcc.Loading(
        dvc.Vega(id='rating_graph', spec={}, style={"height": '24vh', "border": "1px solid lightgrey", "border-bottom-left-radius": "8px", "border-bottom-right-radius": "8px", 'backgroundColor': 'white', 'padding': '2vh', 'paddingRight': '3vh'})))], fluid=True)]
    )], style={"marginTop": "1.5vh", 'width': '100%', 'height': '30vh'})


Purchase_history_chart = html.Div([
    html.Div(['User Purchase History'], style={"textAlign": "left", 'paddingLeft': '2vw', 'paddingTop': '0.5vw', 'paddingBottom': '0.5vw', 'fontWeight': 'bold',"border": "1px solid lightgrey", "border-top-left-radius": "8px", "border-top-right-radius": "8px", 'fontSize': '16px', 'marginLeft': '0.75vw', 'marginRight': '0.75vw'}),
    
    html.Div(
        [dbc.Container([html.Div(dcc.Loading(
            dvc.Vega(id='purchase_graph', spec={}, style={"height": '24vh', "border": "1px solid lightgrey", "border-bottom-left-radius": "8px", "border-bottom-right-radius": "8px", 'backgroundColor': 'white', 'padding': '2vh', 'paddingRight': '3vh'})))], fluid=True)]
    )], style = {"marginTop": "1vh", 'width': '100%', 'height': '30vh'})


Engagement_chart = html.Div([
    html.Div('User Engagement Levels', style={"textAlign": "left", 'paddingLeft': '2vw', 'paddingTop': '0.5vw', 'paddingBottom': '0.5vw', 'fontWeight': 'bold', "border": "1px solid lightgrey", "border-top-left-radius": "8px", "border-top-right-radius": "8px", 'fontSize': '16px', 'marginLeft': '0.75vw', 'marginRight': '0.75vw'}),
    html.Div(
        [dbc.Container([html.Div(dcc.Loading(
            dvc.Vega(id='engagement_graph', spec={}, style={"height": '18vh', "border": "1px solid lightgrey", "border-bottom-left-radius": "8px", "border-bottom-right-radius": "8px", 'backgroundColor': 'white', 'padding': '2vh', 'paddingRight': '3vh'})))], fluid=True)]
    )], style={"marginTop": "1vh", 'width': '100%', 'height': '25vh'})

