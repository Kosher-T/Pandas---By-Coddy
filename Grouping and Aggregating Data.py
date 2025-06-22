# pandas as pd is already imported
df = pd.read_csv("./visits.csv")
# Write your code below
sum_visits = df.groupby("location_id")["visits"].sum()

res = {
    "min": df.groupby("location_id")["visits"].min(),
    "max": df.groupby("location_id")["visits"].max(),
    "mean": df.groupby("location_id")["visits"].mean(),
    "std": df.groupby("location_id")["visits"].std(),
    "median": df.groupby("location_id")["visits"].median(),
    "sum": sum_visits
}

print(res)
