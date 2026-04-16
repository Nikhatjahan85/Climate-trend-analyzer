import pandas as pd


def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
    df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())
    df['Humidity'] = df['Humidity'].fillna(df['Humidity'].mean())

    # SAVE cleaned data
    df.to_csv("data/processed/climate_cleaned.csv", index=False)

    return df