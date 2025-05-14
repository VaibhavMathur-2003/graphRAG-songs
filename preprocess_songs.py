import pandas as pd

# Load your dataset
df = pd.read_csv("spotify_millsongdata.csv")

# Check how many unique artists are in the dataset
print(f"Number of unique artists: {df['artist'].nunique()}")

# Limit to a maximum of 20 rows per artist
df_limited = df.groupby("artist").head(15)

# Save to a new CSV if needed
df_limited.to_csv("songs_processed_data.csv", index=False)

# Optional: Show how many rows are in the new DataFrame
print(f"New DataFrame has {len(df_limited)} rows")
