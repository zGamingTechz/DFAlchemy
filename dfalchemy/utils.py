import pandas as pd

def save_df(df, filename="dataframe.csv"):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Please pass a dataframe")

    if not filename.endswith(".csv"):
        filename += ".csv"
    df.to_csv(filename, index=False)


def info(df):
    print("📊 DataFrame Overview")
    print("-" * 30)
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("🧱 Column Types")
    print(df.dtypes)
    print()

    print("❓ Missing Values")
    missing = df.isnull().sum()
    percent_missing = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing': missing,
        'Percent (%)': percent_missing.round(2)
    })
    print(missing_df[missing_df['Missing'] > 0] if missing.sum() else "No missing values\n")

    print("🔢 Numeric Column Means")
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns
    if len(numeric_cols):
        print(df[numeric_cols].mean().round(2))
    else:
        print("No numeric columns.\n")

    print("\n🔎 Unique Values (≤10 unique)")
    for col in df.columns:
        unique_vals = df[col].nunique()
        if unique_vals <= 10:
            print(f"{col} ({unique_vals}): {df[col].unique()}")
    print()

    print("👁 Preview")
    print(df.head(5))
