# pandas as pd is already imported


df = pd.read_csv("./visits.csv")

# Write your code below
sum_visits = df.groupby("location_id").sum()
min_visits = df.groupby("location_id").min()
max_visits = df.groupby("location_id").max()
mean_visits = df.groupby("location_id").mean()
std_visits = df.groupby("location_id").std()
median_visits = df.groupby("location_id").median()

# Write your code below
sum_visits = sum_visits.rename(columns={"visits": "sum_visits"})[["sum_visits"]]
min_visits = min_visits.rename(columns={"visits": "min_visits"})[["min_visits"]]
max_visits = max_visits.rename(columns={"visits": "max_visits"})[["max_visits"]]
mean_visits = mean_visits.rename(columns={"visits": "mean_visits"})[["mean_visits"]]
std_visits = std_visits.rename(columns={"visits": "std_visits"})[["std_visits"]]
median_visits = median_visits.rename(columns={"visits": "median_visits"})[["median_visits"]]

df = sum_visits.merge(min_visits, on="location_id")
df = df.merge(max_visits, on="location_id")
df = df.merge(mean_visits, on="location_id")
df = df.merge(std_visits, on="location_id")
df = df.merge(median_visits, on="location_id")
