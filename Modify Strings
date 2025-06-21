# pandas as pd is already imported


df = pd.read_csv("./stats.csv")

# Write your code below
df["COLOR"] = df["COLOR"].str.split(" ").str[-1]
df["COUNTRY_LENGTH"] = df["COUNTRY"].astype(str).str.len()
df = df[~(df['SKILL'].str.split().str.len() > 1)]
