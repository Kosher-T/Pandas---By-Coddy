# pandas as pd is already imported
df = pd.read_csv("./missing.csv")
# Write your code below
df = df.drop_duplicates()
for column in df.columns:
    df = df.rename(columns={f"{column}": column.lower()})
df["is_valid"] = df["is_valid"].astype(bool)
