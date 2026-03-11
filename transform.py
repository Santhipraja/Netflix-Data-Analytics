import pandas as pd
from extract import extract_data

def transform_data():
    
    df = extract_data()

    # Convert date column
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Remove missing values
    df = df.dropna(subset=['country'])

    # Create year column
    df['year_added'] = df['date_added'].dt.year

    print("Data Transformation Completed")

    return df

if __name__ == "__main__":
    transform_data()