
import dash_bootstrap_components as dbc
from dash import html, dash_table


Expiring_Members_Table = (dash_table.DataTable(
                            id="expiring-table-placeholder",
                            page_size=14, 
                            style_table={'overflowY': 'auto'},  # Set a larger scrollable height
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

                                        style={"marginTop": "20px"}

                                    )

Expired_Members_Card = dbc.Card(dbc.CardBody(
                                            [
                                                html.H4("Expiring Users", className="card-title"),
                                                html.H3(id="expiring-number-placeholder", className="card-text")
                                            ]
                                        ),
                                        color="danger", 
                                        inverse=True,

                                        style={"marginTop": "20px"}

                                    )
