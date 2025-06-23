# pandas as pd is already imported


df = pd.read_csv("./stats.csv")

# Write your code below
df = df[df["SKILL_POINTS"] > 7]
df = df[(df["UTILIZATION"] <= 0.7)|(df["UTILIZATION"] <= 0.7)]
df = df[df["IS_VALID"] == 1]
df = df[df["CATEGORY"].isin(['JAPE', 'PLQR', 'GHUP'])]
