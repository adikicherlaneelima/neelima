import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df = df[['Date', 'Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    return df.sort_values('Date')

def get_close_prices(df):
    return df['Close'].values