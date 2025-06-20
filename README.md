# 🎵 MoodMapper

**MoodMapper** is a lyrics emotion analysis backend that combines GPT-based language understanding with Genius lyric scraping. It extracts both a summary and the emotional tone of a song based on its lyrics — either pasted directly or retrieved automatically via artist and title.

This project is designed to be extensible, API-first, and integrates clean retry logic to handle LLM variability.

---

## ⚙️ Features

- 🔍 Analyze lyrics with OpenAI (summary + 3–5 emotions)
- 🎤 Fetch lyrics from Genius using artist and title
- 🔁 Automatic retries if GPT output fails to parse
- 📦 Clean modular backend with FastAPI

---

## 🧱 Folder Structure
moodmapper
├── backend/            # FastAPI backend + utils
│   ├── main.py
│   ├── openai_utils.py
│   ├── genius_utils.py
│   └── requirements.txt
├── frontend/           # Placeholder for future React UI
├── scripts/            # For automation, CLI tools, exports, etc.
├── tests/              # Manual test scripts for GPT and Genius APIs
│   ├── test_openai.py
│   └── test_lyricsgenius.py
├── .gitignore
└── README.md

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/moodmapper.git
cd moodmapper
```

### 2. Clone the repo

```
python3 -m venv venvmoodmapper
source venvmoodmapper/bin/activate
```

### 3. Install dependencies

```
cd backend
pip install -r requirements.txt
```

### 4. Add your .env file

```
OPENAI_API_KEY=sk-...
GENIUS_API_TOKEN=your_genius_token
```

### 5. Run the Server

```
uvicorn main:app --reload
```

## API Endpoints

## POST /analyze_lyrics

Analyze raw lyrics directly.

```
{
  "lyrics": "Hello darkness, my old friend..."
}
```

## POST /analyze_song

Provide artist and title, and the server will fetch the lyrics for you.

```
{
  "artist": "Duwap Kaine",
  "title": "Trapaholic Intro"
}
```
## 🔜 Planned Features

•	✅ Frontend UI in React (WIP)
•	✅ CSV export or database logging
•	✅ Emotion trend visualization (timeline, clustering, etc.)
•	✅ Handle genre-specific prompt tuning