import pandas as pd

def save_df(df, filename="dataframe.csv"):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Please pass a dataframe")

    if not filename.endswith(".csv"):
        filename += ".csv"
    df.to_csv(filename, index=False)
