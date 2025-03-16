import pandas as pd
import numpy as np

data = pd.read_csv("data/raw/amazon_prime_users.csv", sep=";", 
                   parse_dates=["Membership Start Date", "Membership End Date", "Date of Birth"], 
                   dayfirst=True)

# Process the data
data["Age"] = (pd.Timestamp.today() - data["Date of Birth"]).dt.days // 365
data["Months Till Expire"] = np.ceil(
    (data["Membership End Date"] - pd.Timestamp.today()).dt.days / 30).clip(lower=0)

data["Membership End Date"] = data["Membership End Date"].dt.date

cols = data.columns[np.r_[4, 8:16]]
data[cols] = data[cols].astype('category')


