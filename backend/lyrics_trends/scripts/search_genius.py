import pandas as pd
from backend.genius_utils import search_genius_song
from pathlib import Path
import time

def search_and_save_genius_matches(input_csv: str, output_csv: str, max_rows=None):
    df = pd.read_csv(input_csv)
    results = []

    print(f"🔍 Starting Genius search for {len(df)} songs...")
    for i, row in df.iterrows():
        if max_rows and i >= max_rows:
            break
        
        title= row['song_title']
        artist = row['artist']
        print(f"{i+1:4d}/{len(df)} Searching: {title} by {artist}")

        match = search_genius_song(artist, title)

        results.append({
            "song_title": title,
            "artist": artist,
            "chart_date": row['chart_date'],
            "year": row['year'],
            "rank": row['rank'],
            "genius_url": match['url'] if match else None,
            "genius_id": match['id'] if match else None,
            "found": bool(match),
        })

        time.sleep(1.2) # Respect rate limits

    out_df = pd.DataFrame(results)
    Path(output_csv).parent.mkdir(parents=True, exists_ok=True)
    out_df.to_csv(output_csv, index=False)
    print(f"✅ Saved Genius matches to {output_csv}")