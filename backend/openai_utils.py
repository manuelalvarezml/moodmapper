import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
print("🔑 Loaded API Key:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def analyze_lyrics_with_openai(
        lyrics: str, 
        max_retries: int = 2) -> dict:
    
    prompt = f"""
        You are a music expert AI. Analyze the following song lyrics.

        1. Give a 1-sentence summary of what the song is about. 
        2. List 3 of 5 emotions that the lyrics evoke. Separate the emotions by commas.
        
        Return first the 1-sentence summary and then the list of emotions in a different line.
        Make sure it is only a different line (sentence \n list) and not a new paragraph (\n\n)
        
        ❌ Do NOT include:
        - Section titles (like 'Summary:' or 'Emotions:' or 'Evoke emotions:')
        - Dashes, asterisks, or numbers
        - Extra newlines (\n\n)

        ✅ Your response must be:
        - One sentence summary
        - Then a single line with 3 to 5 emotions, separated only by commas
        
        Lyrics:
        {lyrics}
        """
    for attempt in range(max_retries + 1):
        try:
            response = client.responses.create(
                model="gpt-3.5-turbo",
                instructions="You analyze song lyrics.",
                input=prompt,
                temperature=0.7,
                max_output_tokens=200
            )
            # Parse
            text = response.output[0].content[0].text
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            summary = lines[0] if len(lines) > 0 else ""
            emotions_line = lines[1] if len(lines) >1 else ""
            emotions = [e.strip() for e in emotions_line.split(",") if e.strip()]
            # To avoid responses like "Emotions: ..." or "Evoked Emotions: ..." on the first element
            emotions[0] = emotions[0].split(" ")[-1] if len(emotions[0].split(" "))>1 else emotions[0]

            if summary and emotions:
                return {
                    "full response":text,
                    "summary":summary,
                    "emotions":emotions,
                }
            print(f"⚠️ GPT output not parseable on attempt {attempt + 1}: {text}")
        
        except Exception as e:
            print(f"💥 OpenAI API error on attempt {attempt + 1}", e)
    
    # If all attempts fail:
    return {
        "full response": "",
        "summary": "", 
        "emotions": [],
        "message": f"All {max_retries + 1} attempts failed."}