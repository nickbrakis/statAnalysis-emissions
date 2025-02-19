import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    """Preprocess the data for analysis."""
    # Example preprocessing steps
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def get_pm10_data(filepath):
    """Load and preprocess PM10 data."""
    df = load_data(filepath)
    df = preprocess_data(df)
    return df