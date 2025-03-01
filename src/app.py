from dash import Dash, html, dcc, Input, Output, callback
from data import processed_data
import dash_bootstrap_components as dbc
import pandas as pd

# Process and load the data directly
df = processed_data()

# Count users
current_users = df[df["Months Till Expire"] > 0].index.nunique()
expired_users = df[df["Months Till Expire"] == 0].index.nunique()

# Filter expiring members
expiring_members = df[["Name", "Email Address", "Membership End Date"]].reset_index()



# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout 
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # Left column for filters
                dbc.Col(
                    [
                        # title
                        html.H1("Amazon Prime Dashboard", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "30px"}),

                        # renewal button
                        html.Label("Renewal Type", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            [
                                dbc.Button("Manual", id="manual-renew", className="me-1", style={"marginBottom": "10px", "width": "100%", "backgroundColor": "#FF9900"}),
                                dbc.Button("Auto Renew", id="auto-renew", style={"marginBottom": "50px", "width": "100%", "backgroundColor": "#FF9900"}),
                            ]

                        ),    
                        #gender button
                        html.Label("Gender", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            [
                                dbc.Button("Male", id="male-gender", className="me-1", style={"marginBottom": "10px", "width": "100%", "backgroundColor": "#FF9900"}),
                                dbc.Button("Female", id="female-gender", style={"marginBottom": "50px", "width": "100%", "backgroundColor": "#FF9900"}),
                            ]
                        ),
                        #age range slider
                        html.Label("Age Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            dcc.RangeSlider(
                                id='age-range-filter',
                                min=0,
                                max=100,
                                step=10,
                            ),
                            style={"marginBottom": "50px"} 
                        ),
                        # date range buttons
                        html.Label("Date Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            [
                                dbc.Button("1 Month", id="1-month-filter", className="me-1", style={"marginBottom": "10px", "width": "100%", "backgroundColor": "#FF9900"}),
                                dbc.Button("3 Month", id="3-month-filter", style={"marginBottom": "10px", "width": "100%", "backgroundColor": "#FF9900"}),
                                dbc.Button("6 Month", id="6-month-filter", style={"marginBottom": "10px", "width": "100%", "backgroundColor": "#FF9900"}),
                                dbc.Button("All Time", id="All-time-filter", style={"marginBottom": "20px", "width": "100%", "backgroundColor": "#FF9900"}),
                            ]
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
                        dbc.Table(id="expiring-table-placeholder", striped=True, bordered=True, hover=True), 

                    ],
                    width=5,  
                ),

                # Right column 
                dbc.Col(
                    [
                        # Placeholder for right column 
                        # Graph Here
                        # ...
   
                    ],
                    width=5,  
                ),
            ]
        )
    ],
    fluid=True,
)


# Callback to update current and expired users 
@app.callback(
    [Output("current-number-placeholder", "children"),
     Output("expiring-number-placeholder", "children"),
     Output("expiring-table-placeholder", "children")],
    [Input("manual-renew", "n_clicks"),
     Input("auto-renew", "n_clicks"),
     Input("male-gender", "n_clicks"),
     Input("female-gender", "n_clicks"),
     Input("age-range-filter", "value"),
     Input("1-month-filter", "n_clicks"),
     Input("3-month-filter", "n_clicks"),
     Input("6-month-filter", "n_clicks"),
     Input("All-time-filter", "n_clicks")]
)
def update_users_and_table(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):
    # Filter based on gender
    gender_filtered = df
    if male_clicks:
        gender_filtered = df[df["Gender"] == "Male"]
    elif female_clicks:
        gender_filtered = df[df["Gender"] == "Female"]

    # Filter based on age range (adjust the age range values)
    if age_range:
        gender_filtered = gender_filtered[gender_filtered["Age"] >= age_range[0]]
        gender_filtered = gender_filtered[gender_filtered["Age"] <= age_range[1]]

    # Filter based on date range (using the 'Months Till Expire' column)
    if month1:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 1]
    elif month3:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 3]
    elif month6:
        gender_filtered = gender_filtered[gender_filtered["Months Till Expire"] <= 6]
    elif all_time:
        gender_filtered = gender_filtered

    # Calculate current and expired users
    current_users = gender_filtered[gender_filtered["Months Till Expire"] > 0].index.nunique()
    expired_users = gender_filtered[gender_filtered["Months Till Expire"] == 0].index.nunique()

    # Prepare the table for expiring members
    expiring_members = gender_filtered[["Name", "Email Address", "Membership End Date"]].reset_index()

    # Return the updated values
    return current_users, expired_users, dbc.Table.from_dataframe(expiring_members, striped=True, bordered=True, hover=True)


# callback for rating overtime graph
@callback(
    Output("rating-overtime-graph-placeholder", "children"),
    Input("manual-renew", "n_clicks"),
    Input("auto-renew", "n_clicks"),
    Input("male-gender", "n_clicks"),
    Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    Input("1-month-filter", "n_clicks"),
    Input("3-month-filter", "n_clicks"),
    Input("6-month-filter", "n_clicks"),
    Input("All-time-filter", "n_clicks"),
)
def update_rating_overtime_graph(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return updated_rating_overtime_graph


# callback for purchase history graph
@callback(
    Output("purchase-history-graph-placeholder", "children"),
    Input("manual-renew", "n_clicks"),
    Input("auto-renew", "n_clicks"),
    Input("male-gender", "n_clicks"),
    Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    Input("1-month-filter", "n_clicks"),
    Input("3-month-filter", "n_clicks"),
    Input("6-month-filter", "n_clicks"),
    Input("All-time-filter", "n_clicks"),
)
def update_rating_overtime_graph(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return updated_purchase_hirtory_graph


# callback for user engagement graph
@callback(
    Output("user-engagement-graph-placeholder", "children"),
    Input("manual-renew", "n_clicks"),
    Input("auto-renew", "n_clicks"),
    Input("male-gender", "n_clicks"),
    Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    Input("1-month-filter", "n_clicks"),
    Input("3-month-filter", "n_clicks"),
    Input("6-month-filter", "n_clicks"),
    Input("All-time-filter", "n_clicks"),
)
def update_user_engagement_graph(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return updated_user_engagement_graph



if __name__ == "__main__":
    app.run(debug=True)
