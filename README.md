## youtube-llamahub-loaders
Repository Description: Welcome to the YouTube LlamaHub Loaders repository! This project demonstrates how to use LlamaHub to load metadata and transcripts of YouTube videos using the `llama_index` library.

## Features

- **YouTube Metadata Loading**: Fetch metadata for YouTube videos.
- **Transcript Loading**: Retrieve the transcripts of YouTube videos.
- **API Integration**: Easily integrate with YouTube Data API.

# YouTube LlamaHub Loaders

Welcome to the YouTube LlamaHub Loaders repository! This project demonstrates how to use LlamaHub to load metadata and transcripts of YouTube videos using the `llama_index` library.

## Features

- **YouTube Metadata Loading**: Fetch metadata for YouTube videos.
- **Transcript Loading**: Retrieve the transcripts of YouTube videos.
- **API Integration**: Seamless integration with YouTube Data API for fetching video details.

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/youtube-llamahub-loaders.git
    cd youtube-llamahub-loaders
    ```

2. **Install dependencies**
    ```bash
    pip install llama_index
    pip install llama_index.readers.youtube_metadata
    pip install llama_index.readers.youtube_transcript
    ```

3. **Set up YouTube API Key**
    - Replace `YOUR_YOUTUBE_API_KEY` in the script with your actual YouTube API key.

## Usage

1. **Run the main script**
    ```python
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
    ```

## Contributing

Feel free to open issues or submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License.

