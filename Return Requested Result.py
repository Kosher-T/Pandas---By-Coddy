import pandas as pd

df = pd.read_csv("./stats.csv")
df = df[1::2]  # Extract only the even ids
df = df[['ID', 'SKILL', 'SKILL_POINTS']]  # Extract only certain columns
# Loop through columns to change names to lower case
df = df.rename(columns={"ID": "id", "SKILL": "skill", "SKILL_POINTS": "skill_points"})  # Maybe I can use .rename({dict}, axis=1)? Check
df = df.sort_values(by='skill_points', ascending=False)  # Sort by skill_points column (now lowercase)
