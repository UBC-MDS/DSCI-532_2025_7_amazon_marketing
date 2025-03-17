
import dash_bootstrap_components as dbc
from dash import html, dash_table


Expiring_Members_Table = (dash_table.DataTable(
                            id="expiring-table-placeholder",
                            page_size=18,
                            style_table={'overflowY': 'auto', 'height': '60vh'},  # Set a larger scrollable height
                            filter_action="native",  # Allow column filtering
                            sort_action="native",  # Allow sorting by column
                            page_action="native",  # Remove pagination and show all rows
                            # Align text in the cells to the left
                            style_cell={'textAlign': 'left',
                                        "fontSize": "0.8vw"},
                            filter_options={"case":"insensitive"},
                            style_header={'fontSize': '0.87vw'}
                        ))

Current_Members_Card = dbc.Card(dbc.CardBody(
                                            [
                                                html.H4("Current Users", className="card-title"),
                                                html.H3(id="current-number-placeholder", className="card-text", style={'fontSize': '1.7vw'})
                                            ]
                                        ),
                                        color="success", 
                                        inverse=True, 

                                style={"marginTop": "2vh", "fontSize": "1.3vw"}

                                    )

Expired_Members_Card = dbc.Card(dbc.CardBody(
                                            [
                                                html.H4("Expiring Users", className="card-title"),
                                                html.H3(id="expiring-number-placeholder", className="card-text", style={'fontSize':'1.7vw'})
                                            ]
                                        ),
                                        color="danger", 
                                        inverse=True,

                                style={"marginTop": "2vh", "fontSize": "1.3vw"}

                                    )
