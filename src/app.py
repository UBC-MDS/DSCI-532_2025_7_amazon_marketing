from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from datetime import datetime
import pandas as pd
import altair as alt


# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Process and load the data directly
def processed_data():
    # Load the raw data
    data = pd.read_csv("data/raw/amazon_prime_users.csv", sep=";", 
                       parse_dates=["Membership Start Date", "Membership End Date", "Date of Birth"], 
                       dayfirst=True)

    # Process the data
    data["Age"] = (pd.Timestamp.today() - data["Date of Birth"]).dt.days // 365
    data["Months Till Expire"] = ((data["Membership End Date"] - pd.Timestamp.today()).dt.days // 30).clip(lower=0)

    data["Membership End Date"] = data["Membership End Date"].dt.date
    # Return the processed DataFrame
    return data

df = processed_data()


# Define the layout of the app
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # Left column for filters
                dbc.Col(
                    [
                        # Title
                        html.H2("Amazon Prime Dashboard", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginTop": "30px", "marginBottom": "30px"}),

                        # Renewal checkboxes 
                        html.Label("Renewal Type", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "20px"}),
                        dbc.Checklist(
                            id="renewal-checklist",
                            options=[
                                {"label": "Manual", "value": "Manual"},
                                {"label": "Auto Renew", "value": "Auto-renew"},
                            ],
                            value=['Manual', 'Auto-renew'],
                            inline=False,  
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",  
                                "fontSize": "16px",  
                                "marginBottom": "30px"
                            }
                        ),

                        # Gender checkboxes 
                        html.Label("Gender", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "20px"}),
                        dbc.Checklist(
                            id="gender-checklist",
                            options=[
                                {"label": "Male", "value": "Male"},
                                {"label": "Female", "value": "Female"},
                            ],
                            value=["Male", "Female"],
                            inline=False, 
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center", 
                                "fontSize": "16px", 
                                "marginBottom": "30px"
                            }
                        ),

                        # Age range slider
                        html.Label("Age Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "20px"}),
                        html.Div(
                            dcc.RangeSlider(
                                id="age-range-filter",
                                min=0,
                                max=100,
                                step=10,
                                value=[0, 100],  
                            ),
                            style={"marginBottom": "20px"}
                        ),

                        # Date range RadioItems 
                        html.Label("Date Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "20px"}),
                        dbc.RadioItems(
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
                        ),
                    ],
                    width=2,
                ),
                # Middle column
                dbc.Col(
                    [
                        # Row for the cards
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H4("Current Users", className="card-title"),
                                                html.H3(id="current-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="success", 
                                        inverse=True, 
                                        style={"marginTop": "30px"}
                                    ),
                                    width=6
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H4("Expired Users", className="card-title"),
                                                html.H3(id="expiring-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="danger", 
                                        inverse=True,
                                        style={"marginTop": "30px"}
                                    ),
                                    width=6
                                ),
                            ]
                        ),

                        # Table for expiring members
                        html.H4("Expiring Members", style={"marginTop": "30px"}),
                        dash_table.DataTable(
                            id="expiring-table-placeholder",
                            columns=[],  # Set the columns dynamically from the filtered DataFrame
                            data=[],  # Convert filtered DataFrame to records for DataTable
                            page_size=20, 
                            style_table={'height': '700px', 'overflowY': 'auto'},  # Set a larger scrollable height
                            filter_action="native",  # Allow column filtering
                            sort_action="native",  # Allow sorting by column
                            page_action="native",  # Remove pagination and show all rows
                            # Align text in the cells to the left
                            style_cell={'textAlign': 'left',
                                        "fontSize": "12px"},
                        ),
                    ],
                    width=5,
                ),
                
                # Right column
                dbc.Col(
                    [
                        # Placeholder for right column
                        html.H4("User Ratings Overview",
                                style={"marginTop": "20px", "textAlign": "left", 'paddingLeft':'30px', 'marginBottom':  '10px'}),
                        dvc.Vega(id='rating_graph', spec={}),
                        html.H4("User Purchase History", style={
                                "marginTop": "20px", "textAlign": "left", 'paddingLeft': '30px', 'marginBottom':  '10px'}),
                        dvc.Vega(id='purchase_graph', spec={}),
                        html.H4("User Engagement Levels", style={
                                "marginTop": "20px", "textAlign": "left", 'paddingLeft': '30px', 'marginBottom':  '10px'}),
                        dvc.Vega(id='engagement_graph', spec={})
                    ],
                    width=5,
                ),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.P(
                            "This app provides insights into user engagement, subscription renewal behavior, and content preferences among Amazon Prime users.",
                            style={"fontSize": "14px", "marginTop": "5px", "textAlign": "center"}
                        ),
                        html.P(
                            "Created by Daduica Julian, Yixuan Gao, and Mavis Wong.",
                            style={"fontSize": "14px", "textAlign": "center"}
                        ),
                        html.P(
                            html.A("View the repository on GitHub", href="https://github.com/UBC-MDS/DSCI-532_2025_7_amazon_marketing", target="_blank"),
                            style={"fontSize": "14px", "textAlign": "center"}
                        ),
                        html.P(
                            f"Latest update: {datetime.now().strftime('%B %d, %Y')}",
                            style={"fontSize": "14px", "textAlign": "center"}
                        ),
                    ], 
                    style={"marginBottom": "14px"},
                ),
                width=12,
            )
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
    df_filtered = df[
        (df['Gender'].isin(gender_values)) &
        (df['Renewal Status'].isin(renewal_values)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'].between(0,date_range_values, 'right'))
    ]
    
    # Calculate current and expired users
    current_users = df[df["Months Till Expire"] > 0].index.nunique()
    
    expired_users = df[df["Months Till Expire"] == 0].index.nunique()

    # Prepare the table for expiring members (only the selected columns)
    expiring_members = df_filtered[["Name", "Email Address", "Membership End Date"]].reset_index()
    
    columns = [{"name": col, "id": col} for col in expiring_members.columns]

    # Return the updated table with filtered data
    return current_users, expired_users, expiring_members.to_dict('records'), columns


# callback for rating distribution graph
@app.callback(
    Output("rating_graph", "spec"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_rating_graph(renew, gender, age_range, date_range):
    df_filtered = df[
        (df['Gender'].isin(gender)) &
        (df['Renewal Status'].isin(renew)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'] <= date_range)
    ]
    rating_graph = alt.Chart(df_filtered).transform_density(
        'Feedback/Ratings',
        groupby = ['Gender'],
        as_ = ['Feedback/Ratings', 'density']
    ).mark_line(strokeWidth=4).encode(
        x = alt.X('Feedback/Ratings', title="Ratings"),
        y = alt.Y('density:Q', title='Density'),
        color=alt.Color('Gender', legend=alt.Legend(symbolStrokeWidth=5)),
        tooltip = ['Feedback/Ratings']
    ).properties(
        width = 375,
        height = 200, 
    ).configure_axis(
        labelFontSize = 14, 
        titleFontSize = 16   
    ).configure_legend(
        labelFontSize = 14,  
        titleFontSize = 16  
    ).interactive().to_dict()

    return rating_graph

# callback for purchase history graph
@app.callback(
    Output("purchase_graph", "spec"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)

def update_purchase_graph(renew, gender, age_range, date_range):
    df_filtered = df[
        (df['Gender'].isin(gender)) &
        (df['Renewal Status'].isin(renew)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'] <= date_range)
    ]
    purchase_graph = alt.Chart(df_filtered).mark_bar(size=50).encode(
        x=alt.X('Purchase History', axis=alt.Axis(labelAngle=0), title="Product Categories"),
        y=alt.Y('count()', title="Count"),
        color=alt.Color('Gender', legend=alt.Legend(symbolSize=200)),
        tooltip=['count()']
    ).properties(
        width=375,
        height=200
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
    ).configure_legend(
        labelFontSize=14,
        titleFontSize=16
    ).interactive().to_dict()
    return purchase_graph

# callback for user engagement graph
@app.callback(
    Output("engagement_graph", "spec"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_engagement_graph(renew, gender, age_range, date_range):
    df_filtered = df[
        (df['Gender'].isin(gender)) &
        (df['Renewal Status'].isin(renew)) &
        (df['Age'].between(age_range[0], age_range[1])) &
        (df['Months Till Expire'] <= date_range)
    ]
    engagement_graph = alt.Chart(df_filtered).mark_bar(size=75).encode(
        x=alt.X('Engagement Metrics', axis=alt.Axis(labelAngle=0),title="Engagment Level"),
        y=alt.Y('count()', title='Count'),
        color=alt.Color('Gender', legend=alt.Legend(symbolSize=200)),
        tooltip=['count()']
    ).properties(
        width=375,
        height=200
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
    ).configure_legend(
        labelFontSize=14,
        titleFontSize=16
    ).interactive().to_dict()
    return engagement_graph

if __name__ == "__main__":
    app.server.run()
