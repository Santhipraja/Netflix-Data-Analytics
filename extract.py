import pandas as pd

def extract_data():

    file_path = r"D:\netflix project\data\bronze\netflix_titles.csv"

    df = pd.read_csv(file_path)

    print("Raw Data Loaded Successfully")
    print(df.head())

    return df

if __name__ == "__main__":
    extract_data()