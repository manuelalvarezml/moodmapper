from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from openai_utils import analyze_lyrics_with_openai
from genius_utils import get_lyrics

app = FastAPI()

class LyricsRequest(BaseModel):
    lyrics: str

class SongRequest(BaseModel):
    artist: str
    title: str

class BatchRequest(BaseModel):
    songs: List[SongRequest]

@app.get("/")
def read_root():
    return {"message": "MoodMapper backend is running!"}

@app.post("/analyze_lyrics")
def analyze_lyrics(request: LyricsRequest):
    result = analyze_lyrics_with_openai(request.lyrics)
    print("🎤 OpenAI result: \n", result)
    return result

@app.post("/analyze_song")
def analyze_song(request: SongRequest):
    lyrics = get_lyrics(request.artist, request.title)
    if not lyrics:
        return{"error": "Lyrics not found"}
    result = analyze_lyrics_with_openai(lyrics)
    return result

@app.post("/analyze_songs_batch")
def analyze_songs_batch(request: BatchRequest):
    results = []

    for song in request.songs:
        lyrics = get_lyrics(song.artist, song.title)
        if not lyrics:
            results.append({
                "artist": song.artist,
                "title": song.title,
                "error": "Lyrics not found.",
            })
            continue
        analysis = analyze_lyrics_with_openai(lyrics)
        results.append({
            "artist": song.artist,
            "title": song.title,
            **analysis
        })
    return{"results": results}