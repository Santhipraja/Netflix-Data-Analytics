import pandas as pd
import os
from transform import transform_data

def load_data():

    df = transform_data()

    # Create folders if not exist
    os.makedirs("../data/silver", exist_ok=True)
    os.makedirs("../data/gold", exist_ok=True)

    # Save cleaned data
    df.to_csv("../data/silver/netflix_cleaned.csv", index=False)

    # Create summary dataset
    summary = df.groupby("type").size().reset_index(name="count")

    summary.to_csv("../data/gold/netflix_summary.csv", index=False)

    print("Data saved successfully!")

if __name__ == "__main__":
    load_data()