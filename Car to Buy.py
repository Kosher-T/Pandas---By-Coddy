# pandas as pd is already imported


df_feat = pd.read_csv("./car_features.csv")
df_stats = pd.read_csv("./car_raw_stats.csv")

# Step 1: Clean the features data based on the rule "Any missing value is considered a 0"
df_feat.fillna(0, inplace=True)

# Step 2: Identify the top 7 brand names by mean popularity, handling ties correctly.
mean_popularity = df_stats.groupby('brand')['popularity'].mean()
top_brand_names = mean_popularity.sort_values(ascending=False).head(7).index.tolist()

# Step 3: Filter df_stats for cars from the top brands AND that meet budget criteria.
candidate_cars = df_stats[
    (df_stats['brand'].isin(top_brand_names)) &
    (df_stats['price'] < 20000) &
    (df_stats['year'] > 2005)
]

# Step 4: Merge the candidate cars with their features.
full_df = pd.merge(candidate_cars, df_feat, on='car_id')

# Step 5: Apply the final, specific feature filters.
final_cars = full_df[
    (full_df['sits'] == 4) &
    (full_df['has_phone_charger'] == 0) &
    (full_df['is_comfortable'] == 1)
]

# Step 6: Sort the final results and save to the required variable 'df'.
df = final_cars.sort_values(by='car_id')
