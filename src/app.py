from dash import Dash, html, dcc, Input, Output, callback
from data import processed_data
import dash_bootstrap_components as dbc

processed_data()

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
                        # Placeholder for middle columns 
                        # Table here
                        # ...

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

# callback for current users number 
@callback(
    Output("current-number-placeholder", "children"),
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
def update_current_users_number(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return updated_current_number

# callback for expiring users number 
@callback(
    Output("expiring-number-placeholder", "children"),
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
def update_expiring_users_number(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return expiring_number

# callback for expiring members table
@callback(
    Output("expiring-table-placeholder", "children"),
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
def update_expiring_members_table(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

    return updated_expiring_members_table

processed_data()

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
