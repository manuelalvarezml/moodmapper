from backend.lyrics_trends.scripts.search_genius import search_and_save_genius_matches

input_path = "~/Documents/Projects/moodmapper/backend/lyrics_trends/data/processed/billboard_clean.csv"
output_path = "~/Documents/Projects/moodmapper/backend/lyrics_trends/data/interim/genius_matches_test.csv"

search_and_save_genius_matches(input_path, output_path, max_rows=20)