from dash import Input, Output, callback_context as ctx
from dash import dcc
from dash.exceptions import PreventUpdate
import pandas as pd
from flask_caching import Cache


cache = Cache(
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'tmp'
    }
)


@cache.memoize()
def register_table_callbacks(app, df):
    
    @app.callback(
        [Output("current-number-placeholder", "children"),
         Output("expiring-number-placeholder", "children"),
         Output("expiring-table-placeholder", "data"),
         Output("expiring-table-placeholder", "columns")],
        [Input("renewal_radiobutton", "value"),
         Input("gender_radiobutton", "value"),
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
        current_users = df[df["Months Till Expire"] > 0]['User ID'].nunique()
        
        expiring_users = df_filtered['User ID'].nunique()

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

    @app.callback(
        Output("download-csv", "data"),
        Input("download-csv-btn", "n_clicks"),
        Input("renewal_radiobutton", "value"),
        Input("gender_radiobutton", "value"),
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
    
