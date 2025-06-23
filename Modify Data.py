# pandas as pd is already imported


df = pd.read_csv("./stats.csv")
# Write your code below

df.loc[(df['IS_VALID'] == 1) & (df['UTILIZATION'] < 0.4), ['ID', 'COUNTRY', 'COLOR' , 'SKILL', 'SKILL_POINTS', 'CATEGORY']] = "MODIFIED"
