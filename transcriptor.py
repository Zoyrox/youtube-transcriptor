from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Inserisci l'ID del video YouTube: ")
transcript = YouTubeTranscriptApi().fetch(video_id, languages=["it", "en"])

for text in transcript:
    print(text.text)