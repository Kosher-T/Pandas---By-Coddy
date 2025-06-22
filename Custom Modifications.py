# pandas as pd is already imported


df = pd.read_csv("./stats.csv")

# Write your code below
df["CATEGORY"] = df["CATEGORY"].map({"SHOW": 0, "TREE": 1, "JAPE": 2, "GHUP": 3, "PLQR": 4})
df["SKILL_MASTERY"] = (df["SKILL_POINTS"] * df["UTILIZATION"]).apply(lambda x: x/4 if x > 5 else x / 2) + df["IS_VALID"]
df = df.sort_values(by="SKILL_MASTERY", ascending=True)
