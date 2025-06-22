# pandas as pd is already imported
df = pd.read_csv("./visits.csv")
# Write your code below

location_5 = df[df["location_id"] == 5]

res = {
    "min": location_5["visits"].min(),
    "max": location_5["visits"].max(),
    "mean": location_5["visits"].mean(),
    "std": location_5["visits"].std(),
    "median": location_5["visits"].median()
}
print(res)
