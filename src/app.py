from dash import Dash, html, dcc, Input, Output, callback
from data import processed_data
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
import pandas as pd

data = processed_data()

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
                        dvc.Vega(id='rating_graph', spec={}),
                        dvc.Vega(id='purchase_graph', spec={}),
                        dvc.Vega(id='engagement_graph', spec={})
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


# callback for rating overtime graph
@callback(
    Output("rating_graph", "spec"),
    # Input("manual-renew", "n_clicks"),
    # Input("auto-renew", "n_clicks"),
    # Input("male-gender", "n_clicks"),
    # Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    # Input("1-month-filter", "n_clicks"),
    # Input("3-month-filter", "n_clicks"),
    # Input("6-month-filter", "n_clicks"),
    # Input("All-time-filter", "n_clicks"),
)
def update_rating_graph(age_range):
    # age_l, age_h = age_range
    # df = data[data['Gender'].isin(gender)]
    # df = data[data['Renewal Status'].isin(renew)]
    # df = data[data['Age'].between(age_l, age_h)]
    # df = data[data['Months Till Expire'] <= expire]
    rating_graph = alt.Chart(data).transform_density(
        'Feedback/Ratings',
        groupby=['Gender'],
        as_=['Feedback/Ratings', 'density'],
        counts=True,
    ).mark_line().encode(
        x=alt.X('Feedback/Ratings'),
        y=alt.Y('density:Q').stack(False),
        color='Gender',
        tooltip=['Feedback/Ratings']
    ).properties(
        width=400,
        height=300
    ).interactive().to_dict()

    return rating_graph


# callback for purchase history graph
@callback(
    Output("purchase_graph", "spec"),
    # Input("manual-renew", "n_clicks"),
    # Input("auto-renew", "n_clicks"),
    # Input("male-gender", "n_clicks"),
    # Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    # Input("1-month-filter", "n_clicks"),
    # Input("3-month-filter", "n_clicks"),
    # Input("6-month-filter", "n_clicks"),
    # Input("All-time-filter", "n_clicks"),
)
def update_purchase_graph(age_range):
    # age_l, age_h = age_range
    # df = data[data['Gender'].isin(gender)]
    # df = data[data['Renewal Status'].isin(renew)]
    # df = data[data['Age'].between(age_l, age_h)]
    # df = data[data['Months Till Expire'] <= expire]
    purchase_graph = alt.Chart(data).mark_bar().encode(
        x=alt.X('Purchase History', axis=alt.Axis(labelAngle=0)),
        y='count()',
        color='Gender',
        tooltip=['count()']
    ).properties(
        width=400,
        height=300
    ).interactive().to_dict()
    return purchase_graph


# callback for user engagement graph
@callback(
    Output("engagement_graph", "spec"),
    # Input("manual-renew", "n_clicks"),
    # Input("auto-renew", "n_clicks"),
    # Input("male-gender", "n_clicks"),
    # Input("female-gender", "n_clicks"),
    Input("age-range-filter", "value"),
    # Input("1-month-filter", "n_clicks"),
    # Input("3-month-filter", "n_clicks"),
    # Input("6-month-filter", "n_clicks"),
    # Input("All-time-filter", "n_clicks"),
)
def update_engagement_graph(age_range):
    # age_l, age_h = age_range
    # df = data[data['Gender'].isin(gender)]
    # df = data[data['Renewal Status'].isin(renew)]
    # df = data[data['Age'].between(age_l, age_h)]
    # df = data[data['Months Till Expire'] <= expire]
    engagement_graph = alt.Chart(data).mark_bar().encode(
        x=alt.X('Engagement Metrics', axis=alt.Axis(labelAngle=0)),
        y='count()',
        color='Gender',
        tooltip=['count()']
    ).properties(
        width=400,
        height=300
    ).interactive().to_dict()
    return engagement_graph



if __name__ == "__main__":
    app.server.run(debug=True)
