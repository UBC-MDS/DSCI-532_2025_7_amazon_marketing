
import dash_bootstrap_components as dbc
from dash import html, dcc
from data.data import data


df = data

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

