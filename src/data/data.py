import pandas as pd
import numpy as np



data = pd.read_feather("data/raw/amazon_prime_users.feather")

# Process the data
today = pd.Timestamp.today()
cols = ['Gender',
        'Renewal Status',
        'Engagement Metrics',
        "Purchase History"]


data[cols] = data[cols].astype('category')

data["Membership End Date"] = pd.to_datetime(data["Membership End Date"], dayfirst=True)
data["Date of Birth"] = pd.to_datetime(
    data["Date of Birth"], dayfirst=True)

data["Age"] = (today - data["Date of Birth"]).dt.days // 365
data["Months Till Expire"] = np.ceil(
    (data["Membership End Date"] - today).dt.days/30
).clip(lower=0).astype('int')

data["Membership End Date"] = data["Membership End Date"].dt.date

