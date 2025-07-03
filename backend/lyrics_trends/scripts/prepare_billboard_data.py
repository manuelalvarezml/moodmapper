from scripts.fetch_billboard import load_and_clean_billboard

csv_path = '~/Documents/Projects/moodmapper/backend/lyrics_trends/data/raw/hot-100-current.csv'
df = load_and_clean_billboard(csv_path)

processed_path = "~/Documents/Projects/moodmapper/backend/lyrics_trends/data/processed/billboard_clean.csv"
df.to_csv(processed_path, index=False)
print(f"Saved cleaned Billboard data to: {processed_path}")