from lyricsgenius import Genius
import os
from dotenv import load_dotenv
import time

load_dotenv()

genius = Genius(os.getenv("LG_CLIENT_ACCESS_TOKEN"))

artist = genius.search_artist("Duwap Kaine", max_songs=3, sort="title")
print(artist.songs)

# Search for Song Lyrics

start_time_method_1 = time.perf_counter()
# Way 1
song = genius.search_song("Fuck the Streets", artist.name)
end_time_method_1 = time.perf_counter()
elapsed_time_1 = end_time_method_1-start_time_method_1
print(f"Time for method 1: {elapsed_time_1}")

print(song.lyrics)

# Way 2
# this will search artist.songs first
# and if not found, uses search_song

start_time_method_2 = time.perf_counter()
song = artist.song("Fuck the Streets")

end_time_method_2 = time.perf_counter()
elapsed_time_2 = end_time_method_2-start_time_method_2
print(f"Time for method 2: {elapsed_time_2}")

print(song.lyrics)