from dash import Dash, html, dcc, Input, Output, callback, dash_table
# from data import processed_data
import dash_bootstrap_components as dbc
from datetime import datetime
import pandas as pd

# Process and load the data directly
def processed_data():
    # Load the raw data
    data = pd.read_csv("data/raw/amazon_prime_users.csv", sep=";", 
                        parse_dates=["Membership Start Date", "Membership End Date", "Date of Birth"], 
                        dayfirst=True, index_col=0)

    # Process the data
    data["Age"] = (pd.Timestamp.today() - data["Date of Birth"]).dt.days // 365
    data["Months Till Expire"] = ((data["Membership End Date"] - pd.Timestamp.today()).dt.days // 30).clip(lower=0)
    
    # Return the processed DataFrame
    return data

df = processed_data()

# Count users
current_users = df[df["Months Till Expire"] > 0].index.nunique()
expired_users = df[df["Months Till Expire"] == 0].index.nunique()

# Filter expiring members
expiring_members = df[["Name", "Email Address", "Membership End Date"]].reset_index()


# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define the columns for the DataTable (dynamically generated)
columns = [{"name": col.replace("_", " ").title(), "id": col} for col in expiring_members.columns]


# Layout
app.layout = dbc.Container(
    [
        # Store component to keep track of active filters
        dcc.Store(id="active-filter-store", data={"renewal": [], "gender": [], "date_range": []}),

        dbc.Row(
            [
                # Left column for filters
                dbc.Col(
                    [
                        # Title
                        html.H1("Amazon Prime Dashboard", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "30px"}),

                        # Renewal checkboxes 
                        html.Label("Renewal Type", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        dbc.Checklist(
                            id="renewal-checklist",
                            options=[
                                {"label": "Manual", "value": "manual-renew"},
                                {"label": "Auto Renew", "value": "auto-renew"},
                            ],
                            value=[],
                            inline=False,  
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",  
                                "fontSize": "20px",  
                                "marginBottom": "50px"
                            }
                        ),

                        # Gender checkboxes 
                        html.Label("Gender", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        dbc.Checklist(
                            id="gender-checklist",
                            options=[
                                {"label": "Male", "value": "male-gender"},
                                {"label": "Female", "value": "female-gender"},
                            ],
                            value=[],
                            inline=False, 
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center", 
                                "fontSize": "20px", 
                                "marginBottom": "50px"
                            }
                        ),

                        # Age range slider
                        html.Label("Age Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            dcc.RangeSlider(
                                id="age-range-filter",
                                min=0,
                                max=100,
                                step=10,
                                value=[0, 100],  
                            ),
                            style={"marginBottom": "50px"}
                        ),

                        # Date range checkboxes 
                        html.Label("Date Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        dbc.Checklist(
                            id="date-range-checklist",
                            options=[
                                {"label": "1 Month", "value": "1-month-filter"},
                                {"label": "3 Month", "value": "3-month-filter"},
                                {"label": "6 Month", "value": "6-month-filter"},
                                {"label": "All Time", "value": "All-time-filter"},
                            ],
                            value=[],
                            inline=False,  
                            style={
                                "display": "flex",
                                "flexDirection": "column",
                                "alignItems": "center",  
                                "fontSize": "20px",  
                                "marginBottom": "50px"
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
                                                html.H2(id="current-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="success", inverse=True
                                    ),
                                    width=6
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.H4("Expired Users", className="card-title"),
                                                html.H2(id="expiring-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="danger", inverse=True
                                    ),
                                    width=6
                                ),
                            ]
                        ),

                        # Table for expiring members
                        html.H4("Expiring Members", style={"marginTop": "30px"}),
                        dash_table.DataTable(
                            id="expiring-table-placeholder",
                            columns=columns,  # Set the columns dynamically from the filtered DataFrame
                            data=expiring_members.to_dict('records'),  # Convert filtered DataFrame to records for DataTable
                            page_size=20, 
                            style_table={'height': '700px', 'overflowY': 'auto'},  # Set a larger scrollable height
                            filter_action="native",  # Allow column filtering
                            sort_action="native",  # Allow sorting by column
                            page_action="native",  # Remove pagination and show all rows
                            style_cell={'textAlign': 'left'},  # Align text in the cells to the left
                        ),
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
                            style={"fontSize": "16px", "marginTop": "1px", "textAlign": "center"}
                        ),
                        html.P(
                            "Created by Daduica Julian, Yixuan Gao, and Mavis Wong.",
                            style={"fontSize": "16px", "textAlign": "center"}
                        ),
                        html.P(
                            html.A("View the repository on GitHub", href="https://github.com/UBC-MDS/DSCI-532_2025_7_amazon_marketing", target="_blank"),
                            style={"fontSize": "16px", "textAlign": "center"}
                        ),
                        html.P(
                            f"Latest update: {datetime.now().strftime('%B %d, %Y')}",
                            style={"fontSize": "16px", "textAlign": "center"}
                        ),
                    ], 
                    style={"marginBottom": "20px"},
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
     Output("expiring-table-placeholder", "data")],
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_users_and_table(renewal_values, gender_values, age_range, date_range_values):
    # Start with the entire dataset
    gender_filtered = df

    # Apply renewal filter
    if "manual-renew" in renewal_values:
        gender_filtered = gender_filtered[gender_filtered["Renewal Status"] == "Manual"]
    if "auto-renew" in renewal_values:
        gender_filtered = gender_filtered[gender_filtered["Renewal Status"] == "Auto-renew"]

    # Apply gender filter
    if "male-gender" in gender_values:
        gender_filtered = gender_filtered[gender_filtered["Gender"] == "Male"]
    if "female-gender" in gender_values:
        gender_filtered = gender_filtered[gender_filtered["Gender"] == "Female"]

    # Apply age range filter
    if age_range:
        gender_filtered = gender_filtered[(gender_filtered["Age"] >= age_range[0]) & (gender_filtered["Age"] <= age_range[1])]

    # Apply expiration date range filter
    if "1-month-filter" in date_range_values:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 1]
    if "3-month-filter" in date_range_values:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 3]
    if "6-month-filter" in date_range_values:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 6]
    if "All-time-filter" in date_range_values:
        pass  # No filter for all time

    # Calculate current and expired users
    current_users = gender_filtered[gender_filtered["Months Till Expire"] > 0].index.nunique()
    expired_users = gender_filtered[gender_filtered["Months Till Expire"] == 0].index.nunique()

    # Prepare the table for expiring members (only the selected columns)
    expiring_members = gender_filtered[["Name", "Email Address", "Membership End Date"]].reset_index()

    # Return the updated table with filtered data
    return current_users, expired_users, expiring_members.to_dict('records')


# callback for rating overtime graph
@callback(
    Output("rating-overtime-graph-placeholder", "children"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_rating_overtime_graph(renewal_values, gender_values, age_range, date_range_values):

    return updated_rating_overtime_graph


# callback for purchase history graph
@callback(
    Output("purchase-history-graph-placeholder", "children"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_rating_overtime_graph(renewal_values, gender_values, age_range, date_range_values):

    return updated_purchase_hirtory_graph


# callback for user engagement graph
@callback(
    Output("user-engagement-graph-placeholder", "children"),
    [Input("renewal-checklist", "value"),
     Input("gender-checklist", "value"),
     Input("age-range-filter", "value"),
     Input("date-range-checklist", "value")]
)
def update_user_engagement_graph(renewal_values, gender_values, age_range, date_range_values):

    return updated_user_engagement_graph


if __name__ == "__main__":
    app.run(debug=True)

