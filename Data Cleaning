# pandas as pd is already imported
df = pd.read_csv("./missing.csv")
# Write your code below
for column, missing_val in df.isna().sum().items():  # (column, record)
    if missing_val > 2:
        df[column] = df[column].fillna("Missing")

df = df.dropna()
