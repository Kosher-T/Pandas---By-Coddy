# pandas as pd is already imported


df = pd.read_csv("./visits.csv")

# Write your code below
df = df.groupby("location_id").agg({
    "visits": "sum",
    "timestamp": "mean"
})
df = df.rename({"visits": "sum_visits", "timestamp": "mean_timestamp"})
