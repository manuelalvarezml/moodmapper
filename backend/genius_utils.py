import os
import lyricsgenius
from dotenv import load_dotenv

load_dotenv()

genius = lyricsgenius.Genius(os.getenv("LG_CLIENT_ACCESS_TOKEN"), 
                             skip_non_songs=True, 
                             excluded_terms = ["(Remix)","(Live)"])

def get_lyrics(
        artist: str, 
        title:str) -> str:
    try:
        song = genius.search_song(title, artist)
        if song and song.lyrics:
            return song.lyrics
        else:
            return "Song or song lyrics not found"
    except Exception as e:
        print()
        return ""
    
def search_genius_song(artist: str, title: str) -> dict:
    """
    Search Genius and return basic song metadata: id, url, title, and artist.
    """
    try:
        song = genius.seach_song(title, artist)
        if song:
            return {
                "title": song.title,
                "artist": song.artist,
                "id": song.id,
                "url": song.url,
            }
        return None
    except Exception as e:
        print(f"⚠️ Error searching Genius for {title} by {artist}: {e}")
        return None