
---

### `youtube_dl.py` Code

Below is the implementation of `youtube_dl.py` that matches the described functionality, using `pytube` for downloading YouTube videos, with resolution selection, automatic renaming, progress bar, and error handling.

```python
import argparse
import os
import re
from pytube import YouTube
from pytube.cli import on_progress

def sanitize_filename(filename):
    """Sanitize video title to create a valid filename."""
    # Remove invalid characters and replace spaces with underscores
    return re.sub(r'[^\w\s-]', '', filename).strip().replace(' ', '_')

def download_video(url, resolution=None):
    """Download a YouTube video with the specified resolution."""
    try:
        # Initialize YouTube object
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Fetching video: \"{yt.title}\"")

        # Get available video streams (progressive for video+audio)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        available_resolutions = [stream.resolution for stream in streams if stream.resolution]

        if not available_resolutions:
            print("Error: No progressive MP4 streams available.")
            return

        # Display available resolutions
        print(f"Available resolutions: {', '.join(available_resolutions)}")

        # If resolution not provided, prompt user
        if not resolution:
            resolution = input("Enter resolution (e.g., 720p): ").strip()

        # Validate resolution
        if resolution not in available_resolutions:
            print(f"Error: Resolution {resolution} not available. Choose from {available_resolutions}")
            return

        # Select the stream
        stream = streams.filter(resolution=resolution).first()
        if not stream:
            print(f"Error: Could not find stream for resolution {resolution}.")
            return

        # Sanitize video title for filename
        filename = f"{sanitize_filename(yt.title)}.mp4"

        # Download the video
        print("Downloading...")
        stream.download(filename=filename)
        print(f"Video saved as: {filename}")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Please check the URL, network connection, or try a different resolution.")

def main():
    print("🎧 YouTube Video Downloader")
    parser = argparse.ArgumentParser(description="Download YouTube videos from the command line.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--resolution", "-r", help="Resolution (e.g., 720p)", default=None)
    
    args = parser.parse_args()
    
    download_video(args.url, args.resolution)

if __name__ == "__main__":
    main()
