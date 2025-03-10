import dash_bootstrap_components as dbc
import dash_vega_components as dvc

Ratings_chart = dbc.Card(
    [dbc.CardHeader('User Ratings Overview',
                    style={"textAlign": "left",
                           'paddingLeft': '20px',
                           'fontWeight': 'bold'}),
     dbc.CardBody(dvc.Vega(id='rating_graph', spec={}))],
     style={'width': '100%','height': '32%', 'marginTop': '20px'})

Purchase_history_chart = dbc.Card(
    [dbc.CardHeader('User Purchase History',
                    style={"textAlign": "left",
                          'paddingLeft': '20px', 
                          'fontWeight': 'bold'}),
     dbc.CardBody(dvc.Vega(id='purchase_graph', spec={}))],
     style={"marginTop": "10px", 'width': '100%', 'height': '32%'})

Engagement_chart = dbc.Card(
    [dbc.CardHeader('User Engagement Levels',
                    style={"textAlign": "left",
                           'fontWeight': 'bold'}),
    dbc.CardBody(dvc.Vega(id='engagement_graph', spec={}))],
    style={"marginTop": "10px", 'width': '100%', 'height': '27%'})
