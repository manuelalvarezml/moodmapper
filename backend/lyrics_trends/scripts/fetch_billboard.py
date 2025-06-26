import pandas as pd
from pathlib import Path

def load_and_clean_billboard(csv_path: str) -> pd.DataFrame:
    """
    Load and normalize the Billboard Hot 100 dataset.

    Args:
        csv_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Cleaned dataframe with selected columns and normalized text
    """
    df = pd.read_csv(csv_path)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]

    # Rename key columns for consistency
    df.rename(columns={
        'title': 'song_title',
        'performer': 'artist',
        'chart_week': 'chart_date',
        'current_week': 'rank',
    }, inplace=True)

    # Drop rows with missing title or artist 
    df.dropna(subset=['song_title', 'artist'], inplace=True)

    # Strip whitespace
    df['song_title'] = df['song_title'].str.strip()
    df['artist'] = df['artist'].str.strip()

    # Create lowercase versions for matching
    df['song_title_clean'] = df['song_title'].str.lower()
    df['artist_clean'] = df['artist'].str.lower()

    # Add year column for easy grouping
    df['year'] = pd.to_datetime(df['chart_date']).dt.year

    # Sort chronologically
    df = df.sort_values(by=["chart_date", "rank"]).reset_index(drop=True)

    return df[['chart_date', 'year', 'rank', 'song_title', 'artist', 
               'song_title_clean', 'artist_clean']]