# pandas as pd is already imported
df = pd.read_csv("./stats.csv")

# Write your code below
df["SINGLE_VALUE"] = 0
df = df.drop(["COUNTRY", "COLOR"], axis=1)
df.loc[len(df)] = {"ID": 21, "SKILL": "Craft", "SKILL_POINTS": 13, "UTILIZATION": 0.1352, "IS_VALID": 1, "CATEGORY": "SHOW", "SINGLE_VALUE": 0}
df = df.drop(0, axis=0)
