from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from datetime import datetime

from .data import data
from .components import renewal_checkbox, gender_checkbox, age_range_slider, date_range_radio, download_csv
from .components import Expiring_Members_Table, Current_Members_Card, Expired_Members_Card
from .callbacks import register_chart_callbacks
from .callbacks import register_table_callbacks

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = data

# Define the layout of the app
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # Left column for filters
                dbc.Col(
                    [
                        # Title
                        html.H2("Amazon Prime Dashboard", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginTop": "10px", "marginBottom": "20px", "fontSize": "36px"}),

                        # Renewal checkboxes 
                        html.Label("Renewal Type", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "5px", "fontSize": "20px"}),
                        (renewal_checkbox), 

                        # Gender checkboxes 
                        html.Label("Gender", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "5px", "fontSize": "20px"}),
                        (gender_checkbox),

                        # Age range slider
                        html.Label("Age Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "5px", "fontSize": "20px"}),
                        (age_range_slider),
                        
                        # Date range RadioItems 
                        html.Label("Date Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "5px", "fontSize": "20px"}),
                        (date_range_radio),
                    ],
                    width=2,
                    style={"backgroundColor": "#FF9900", "padding": "10px", "borderRadius": "10px"},  
                ),

                # Middle column
                dbc.Col(
                    [
                        # Row for the cards
                        dbc.Row(
                            [
                                dbc.Col(
                                (Current_Members_Card),
                                    width=6
                                ),
                                dbc.Col((Expired_Members_Card),
                                    width=6, 
                                ),
                            ]
                        ),
                        # Table for expiring members
                        html.H2("Expiring Members", style={"marginTop": "50px"}),
                        (Expiring_Members_Table),
                        html.Div(
                            dbc.Button("Download CSV", id="download-csv-btn", color="primary", className="mt-2"),
                            style={"textAlign": "center", "marginTop": "10px"}
                        ),
                        dcc.Download(id="download-csv"),
                    ],
                    width=5,
                    style={"backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "10px"}  
                ),
                
                # Right column
                dbc.Col(
                    [
                        dbc.Card([
                            dbc.CardHeader('User Ratings Overview',
                                           style={"textAlign": "left",
                                                  'paddingLeft': '20px',
                                                  'fontWeight': 'bold'}),
                            dbc.CardBody(
                                dvc.Vega(id='rating_graph',spec={}))], 
                            style={'width': '100%', 
                                   'height':'32%'}),
                                
                        dbc.Card([
                            dbc.CardHeader('User Purchase History', 
                                           style={"textAlign": "left",
                                                  'paddingLeft': '20px', 'fontWeight': 'bold'}),
                                                
                            dbc.CardBody(
                                dvc.Vega(id='purchase_graph', spec={}))],
                            style={"marginTop": "5px", 
                                   'width': '100%', 
                                   'height': '32%'}),
                                
                        dbc.Card([
                            dbc.CardHeader('User Engagement Levels', 
                                           style={"textAlign": "left",
                                                  'paddingLeft': '20px', 'fontWeight': 'bold'}),
                            dbc.CardBody(
                                dvc.Vega(id='engagement_graph', spec={}))],
                            style={"marginTop": "5px", 
                                   'width': '100%', 
                                   'height': '26%'}),
                    ],
                    width=5,
                ),
            ], 
            style={"backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "10px"} 
        ),
        dbc.Row(
            [
                dbc.Col(html.P(
                    "This app provides insights into user engagement, subscription renewal behavior, and content preferences among Amazon Prime users.",
                    style={"fontSize": "14px", "textAlign": "center"}
                ), width="auto"),

                dbc.Col(html.P(
                    "Created by Daduica Julian, Yixuan Gao, and Mavis Wong.",
                    style={"fontSize": "14px", "textAlign": "center"}
                ), width="auto"),

                dbc.Col(html.P(
                    html.A("View the repository on GitHub", href="https://github.com/UBC-MDS/DSCI-532_2025_7_amazon_marketing", target="_blank"),
                    style={"fontSize": "14px", "textAlign": "center"}
                ), width="auto"),

                dbc.Col(html.P(
                    f"Latest update: {datetime.now().strftime('%B %d, %Y')}",
                    style={"fontSize": "14px", "textAlign": "center"}
                ), width="auto"),
            ],
            justify="center",  
            style={"marginTop": "10px", "marginBottom": "10px"} 
        ),
    ],
    fluid=True,
)

register_chart_callbacks(app)
register_table_callbacks(app, df)

if __name__ == "__main__":
    app.server.run(debug = True)
