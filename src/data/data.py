import pandas as pd
import numpy as np



data = pd.read_feather("data/raw/amazon_prime_users.feather")

# Process the data
today = pd.Timestamp.today()
dates = ["Membership End Date", "Date of Birth"]
cols = ['Gender',
        'Renewal Status',
        'Engagement Metrics',
        "Purchase History"]


data[cols] = data[cols].astype('category')
data[dates] = data[dates].astype('date32[pyarrow]')

data["Age"] = (today - data["Date of Birth"]).dt.days // 365
data["Months Till Expire"] = np.ceil(
    (data["Membership End Date"] - today).dt.days/30
).clip(lower=0).astype('int')


