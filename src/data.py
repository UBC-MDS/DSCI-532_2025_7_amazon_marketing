import pandas as pd

def processed_data():
    data = pd.read_csv("../data/raw/amazon_prime_users.csv", sep=";",
                    parse_dates=["Membership Start Date", "Membership End Date", "Date of Birth"], dayfirst=True, index_col=0)

    data["Age"] = (pd.Timestamp.today() - data["Date of Birth"]).dt.days//365

    data["Months Till Expire"] = (
        (data["Membership End Date"] - pd.Timestamp.today()).dt.days//30).clip(lower=0)

    data.to_csv('../data/processed/processed.csv')
    
    
