"""
YouTube LlamaHub Loaders

This script loads metadata and transcripts of YouTube videos using the llama_index library.
"""

from llama_index.readers.youtube_transcript import YoutubeTranscriptReader
from llama_index.readers.youtube_metadata import YouTubeMetaData
from llama_index.readers.youtube_metadata import YouTubeMetaDataAndTranscript

# Replace 'YOUR_YOUTUBE_API_KEY' with your actual YouTube API key
youtube_loader = YouTubeMetaDataAndTranscript(api_key="YOUR_YOUTUBE_API_KEY")

# Specify the video IDs for which you want to fetch data
video_ids = ["ybeBu17aLOM"]  # Replace with actual video IDs

# Load data for the specified video IDs
video_data = youtube_loader.load_data(video_ids)

# Print the fetched data
for video_id, data in video_data.items():
    print(f"Video ID: {video_id}")
    print("Metadata:")
    for key, value in data["metadata"].items():
        print(f"{key}: {value}")
    print("Transcript:")
    print(data["transcript"])
    print("-----------------------------")
