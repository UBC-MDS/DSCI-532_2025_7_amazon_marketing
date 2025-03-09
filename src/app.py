from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from datetime import datetime
import pandas as pd
import altair as alt
import numpy as np
from dash import callback_context as ctx
from dash.exceptions import PreventUpdate


# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Process and load the data directly
def processed_data():
    # Load the raw data
    data = pd.read_csv("data/raw/amazon_prime_users.csv", sep=";", 
                       parse_dates=["Membership Start Date", "Membership End Date", "Date of Birth"], 
                       dayfirst=True)

    # Process the data
    data["Age"] = (pd.Timestamp.today() - data["Date of Birth"]).dt.days // 365
    data["Months Till Expire"] = np.ceil(
        (data["Membership End Date"] - pd.Timestamp.today()).dt.days / 30).clip(lower=0)

    data["Membership End Date"] = data["Membership End Date"].dt.date
    # Return the processed DataFrame
    return data

df = processed_data()

renewal_checkbox = dbc.RadioItems(
                            id="renewal-checklist",
                            options=[
                                {"label": "Manual", "value": "Manual"},
                                {"label": "Auto Renew", "value": "Auto-renew"},
                                {"label": "Both", "value": "Both-Manual-Auto-renew"},
                            ],
                            value="Both-Manual-Auto-renew",
                            inline=False,  
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "start",  
                                "justifyContent": "center",
                                "fontSize": "16px",  
                                "paddingLeft": "50px",  
                                "marginBottom": "20px"
                            }
                        )

gender_checkbox = dbc.RadioItems(
                            id="gender-checklist",
                            options=[
                                {"label": "Male", "value": "Male"},
                                {"label": "Female", "value": "Female"},
                                {"label": "Both", "value": "Both-Male-Female"},

                            ],
                            value="Both-Male-Female",
                            inline=False, 
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "start",  
                                "justifyContent": "center",
                                "fontSize": "16px",  
                                "paddingLeft": "50px",  
                                "marginBottom": "20px"
                            }
                        )

age_range_slider = html.Div(dcc.RangeSlider(
                                id="age-range-filter",
                                min=df["Age"].min(),
                                max=df["Age"].max(),
                                step=1,
                                marks={i: str(i) for i in range(15, df["Age"].max(), 10)},
                                value=[0, 100],  
                                tooltip={"placement": "bottom", "always_visible": True, "style": {"fontSize": "16px"}},
                            ), 
                            style={"marginBottom": "20px"},
                            )

date_range_radio = dbc.RadioItems(
                            id="date-range-checklist",
                            options=[
                                {"label": "1 Month", "value": 1},
                                {"label": "3 Month", "value": 3},
                                {"label": "6 Month", "value": 6},
                                {"label": "All Time", "value": 999},
                            ],
                            value=999,
                            inline=False,  
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",  
                                "fontSize": "16px",  
                                "marginBottom": "20px"
                            }
                        )


Expiring_Members_Table = (dash_table.DataTable(
                            id="expiring-table-placeholder",
                            page_size=20, 
                            style_table={'height': '360px', 'overflowY': 'auto'},  # Set a larger scrollable height
                            filter_action="native",  # Allow column filtering
                            sort_action="native",  # Allow sorting by column
                            page_action="native",  # Remove pagination and show all rows
                            # Align text in the cells to the left
                            style_cell={'textAlign': 'left',
                                        "fontSize": "12px"},
                        ))

Current_Members_Card = dbc.Card(dbc.CardBody(
                                            [
                                                html.H4("Current Users", className="card-title"),
                                                html.H3(id="current-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="success", 
                                        inverse=True, 

                                        style={"marginTop": "30px"}

                                    )

Expired_Members_Card = dbc.Card(dbc.CardBody(
                                            [
                                                html.H4("Expired Users", className="card-title"),
                                                html.H3(id="expiring-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="danger", 
                                        inverse=True,

                                        style={"marginTop": "30px"}

                                    )

download_csv = dbc.Row(
    dbc.Col(
        [
            dbc.Button("Download CSV", id="download-csv-btn", color="primary", className="mt-2"),
            dcc.Download(id="download-csv")
        ],
        width="auto",
        className="text-center"
    )
)

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
                        # Placeholder for right column
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


# Callback to update current and expired users 
@app.callback(
    [Output("current-number-placeholder", "children"),
     Output("expiring-number-placeholder", "children"),
     Output("expiring-table-placeholder", "data"),
     Output("expiring-table-placeholder", "columns")],
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_users_and_table(renewal_values, gender_values, age_range, date_range_values):
    # Start with the entire dataset
    if renewal_values == "Both-Manual-Auto-renew":
        renewal_values = ['Auto-renew', 'Manual']
    else:
        renewal_values = [renewal_values]
    
    if gender_values == "Both-Male-Female":
        gender_values = ['Male', 'Female']
    else:
        gender_values = [gender_values]
        
    df_filtered = df[
        (df['Gender'].isin(gender_values)) &
        (df['Renewal Status'].isin(renewal_values)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'].between(0,date_range_values, 'right'))
    ]
    
    # Calculate current and expired users
    current_users = df[df["Months Till Expire"] > 0].index.nunique()
    
    expiring_users = df_filtered.index.nunique()

    # Prepare the table for expiring members (only the selected columns)
    expiring_members = df_filtered[[
        "User ID", "Name", "Email Address", "Membership End Date", "Gender", "Purchase History", "Engagement Metrics", "Feedback/Ratings"]]
    
    columns_type = [
        ("User ID", "numeric"), ("Name", "text"), 
        ("Email Address","text"), ("Membership End Date", "datetime")
        ]
    columns = [
        {"name": col, "id": col, "type": type} for col, type in columns_type
    ]

    # Return the updated table with filtered data
    return current_users, expiring_users, expiring_members.to_dict('records'), columns

# Callback for downloading csv file
@app.callback(
    Output("download-csv", "data"),
    Input("download-csv-btn", "n_clicks"),
    Input("renewal-checklist", "value"),
    Input("gender-checklist", "value"),
    Input("age-range-filter", "value"),
    Input("date-range-checklist", "value"),
    prevent_initial_call=True
)
def download_csv(n_clicks, renewal_values, gender_values, age_range, date_range_values):
    if not ctx.triggered or ctx.triggered[0]["prop_id"] != "download-csv-btn.n_clicks":
        raise PreventUpdate

    if renewal_values == "Both-Manual-Auto-renew":
        renewal_values = ['Auto-renew', 'Manual']
    else:
        renewal_values = [renewal_values]

    if gender_values == "Both-Male-Female":
        gender_values = ['Male', 'Female']
    else:
        gender_values = [gender_values]
    
    df_filtered = df[
        (df['Gender'].isin(gender_values)) &
        (df['Renewal Status'].isin(renewal_values)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'] <= date_range_values)
    ]

    expiring_members = df_filtered[["User ID", "Name", "Email Address", "Membership End Date"]].reset_index(drop=True)
    return dcc.send_data_frame(expiring_members.to_csv, "Expiring_Members.csv", index=False)

# callback for rating distribution graph
@app.callback(
    Output("rating_graph", "spec"),
    Input("expiring-table-placeholder", "derived_virtual_data")
)
def update_rating_graph(data):
    data = pd.DataFrame(data)
    rating_graph = alt.Chart(data, width='container').transform_density(
        'Feedback/Ratings',
        groupby = ['Gender'],
        as_ = ['Feedback/Ratings', 'density']
    ).mark_line(strokeWidth=3).encode(
        x=alt.X('Feedback/Ratings', title="Ratings"),
        y = alt.Y('density:Q', title='Density'),
        color=alt.Color('Gender', 
                        legend=alt.Legend(symbolStrokeWidth=5), scale=alt.Scale(
                            domain=['Male', 'Female'], 
                            range=['dodgerblue', 'crimson'])),
        tooltip=[alt.Tooltip('Gender'),
                 alt.Tooltip('Feedback/Ratings', title='Ratings'),
                 alt.Tooltip('density:Q', title='Density')]
    ).properties(
        height = 110, 
    ).configure_axis(
        labelFontSize = 12, 
        titleFontSize = 14  
    ).configure_legend(
        labelFontSize = 12,  
        titleFontSize = 14  
    ).to_dict()

    return rating_graph

# callback for purchase history graph
@app.callback(
    Output("purchase_graph", "spec"),
    Input("expiring-table-placeholder", "derived_virtual_data")
)

def update_purchase_graph(data):
    data = pd.DataFrame(data)
    purchase_graph = alt.Chart(data, width='container').mark_bar(size=40).encode(
        x=alt.X('Purchase History', 
                axis=alt.Axis(labelAngle=0), 
                title="Product Categories"),
        y=alt.Y('count()', title="Count"),
        color=alt.Color('Gender', 
                        legend=alt.Legend(symbolSize=200), 
                        scale=alt.Scale(
                            domain=['Male', 'Female'], 
                            range=['dodgerblue', 'crimson'])),
        tooltip=[alt.Tooltip('Gender'),
                 alt.Tooltip('count()', title='Count')],
        order=alt.Order('Gender:N', sort='ascending')
    ).properties(
        height=110
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=14
    ).to_dict()
    return purchase_graph

# callback for user engagement graph
@app.callback(
    Output("engagement_graph", "spec"),
    Input("expiring-table-placeholder", "derived_virtual_data")
)
def update_engagement_graph(data):
    data = pd.DataFrame(data)
    engagement_graph = alt.Chart(data, width='container').mark_bar(size=15).encode(
        y=alt.Y('Engagement Metrics', 
                sort=['High', 'Medium', 'Low'],
                title=None),
        x=alt.X('count()', title='Count'),
        color=alt.Color('Gender', 
                        legend=alt.Legend(symbolSize=200), 
                        scale=alt.Scale(
                            domain=['Male', 'Female'], 
                            range=['dodgerblue', 'crimson'])),
        tooltip=[alt.Tooltip('Gender'),
                 alt.Tooltip('count()', title='Count')],
        order=alt.Order('Gender:N', sort='ascending')
    ).properties(
        height=70
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_legend(
        labelFontSize=12,
        titleFontSize=14
    ).to_dict()
    return engagement_graph

if __name__ == "__main__":
    app.server.run(debug = True)