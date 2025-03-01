from dash import Dash, html, dcc, Input, Output, callback
from data import processed_data
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
import pandas as pd


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
                                dcc.Checklist(
                                    id='renew-filter', 
                                    options=["Auto-renew", "Manual"],
                                    value=["Auto-renew", "Manual"],
                                    style={"marginBottom": "50px"},
                                )
                            ]

                        ),    
                        #gender button
                        html.Label("Gender", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            [
                                dcc.Checklist(
                                    id='gender-filter',
                                    options=["Male", "Female"],
                                    value=["Male", "Female"],
                                    style={"marginBottom": "50px"},
                                )
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
                                value=[10, 100],
                            ),
                            style={"marginBottom": "50px"} 
                        ),
                        # date range buttons
                        html.Label("Date Range", style={"fontWeight": "bold", "textAlign": "center", "display": "block", "marginBottom": "10px", "fontSize": "24px"}),
                        html.Div(
                            [
                                dcc.RadioItems(
                                    id="date-filter",
                                    options=[
                                        {"label": "1 Month", "value":1},
                                        {"label": "3 Month", "value":3},
                                        {"label": "6 Month", "value":6},
                                        {"label": "All Time", "value": 999}],
                                    value=999,
                                ),
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

# # callback for current users number 
# @callback(
#     Output("current-number-placeholder", "children"),
#     Input("manual-renew", "n_clicks"),
#     Input("auto-renew", "n_clicks"),
#     Input("male-gender", "n_clicks"),
#     Input("female-gender", "n_clicks"),
#     Input("age-range-filter", "value"),
#     Input("1-month-filter", "n_clicks"),
#     Input("3-month-filter", "n_clicks"),
#     Input("6-month-filter", "n_clicks"),
#     Input("All-time-filter", "n_clicks"),
# )
# def update_current_users_number(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

#     return updated_current_number

# # callback for expiring users number 
# @callback(
#     Output("expiring-number-placeholder", "children"),
#     Input("manual-renew", "n_clicks"),
#     Input("auto-renew", "n_clicks"),
#     Input("male-gender", "n_clicks"),
#     Input("female-gender", "n_clicks"),
#     Input("age-range-filter", "value"),
#     Input("1-month-filter", "n_clicks"),
#     Input("3-month-filter", "n_clicks"),
#     Input("6-month-filter", "n_clicks"),
#     Input("All-time-filter", "n_clicks"),
# )
# def update_expiring_users_number(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

#     return expiring_number

# # callback for expiring members table
# @callback(
#     Output("expiring-table-placeholder", "children"),
#     Input("manual-renew", "n_clicks"),
#     Input("auto-renew", "n_clicks"),
#     Input("male-gender", "n_clicks"),
#     Input("female-gender", "n_clicks"),
#     Input("age-range-filter", "value"),
#     Input("1-month-filter", "n_clicks"),
#     Input("3-month-filter", "n_clicks"),
#     Input("6-month-filter", "n_clicks"),
#     Input("All-time-filter", "n_clicks"),
# )
# def update_expiring_members_table(manual_clicks, auto_renew_clicks, male_clicks, female_clicks, age_range, month1, month3, month6, all_time):

#     return updated_expiring_members_table



# callback for rating overtime graph
@callback(
    Output("rating_graph", "spec"),
    Input("renew-filter", "value"),
    Input("gender-filter", "value"),
    Input("age-range-filter", "value"),
    Input("date-filter", "value"),
)

def update_rating_graph(renew, gender, age_range, date_range):
    data = processed_data()
    df = data[
        (data['Gender'].isin(gender)) &
        (data['Renewal Status'].isin(renew)) &
        (data['Age'].between(age_range[0], age_range[1])) &
        (data['Months Till Expire'] <= date_range)
    ]
    rating_graph = alt.Chart(df).transform_density(
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
    Input("renew-filter", "value"),
    Input("gender-filter", "value"),
    Input("age-range-filter", "value"),
    Input("date-filter", "value"),
)
def update_purchase_graph(renew, gender, age_range, date_range):
    data = processed_data()
    df = data[
        (data['Gender'].isin(gender)) &
        (data['Renewal Status'].isin(renew)) &
        (data['Age'].between(age_range[0], age_range[1])) &
        (data['Months Till Expire'] <= date_range)
    ]
    purchase_graph = alt.Chart(df).mark_bar().encode(
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
    Input("renew-filter", "value"),
    Input("gender-filter", "value"),
    Input("age-range-filter", "value"),
    Input("date-filter", "value"),
)
def update_engagement_graph(renew, gender, age_range, date_range):
    data = processed_data()
    df = data[
        (data['Gender'].isin(gender)) &
        (data['Renewal Status'].isin(renew)) &
        (data['Age'].between(age_range[0], age_range[1])) &
        (data['Months Till Expire'] <= date_range)
    ]
    engagement_graph = alt.Chart(df).mark_bar().encode(
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
    app.server.run(debug=True, port=8081)


