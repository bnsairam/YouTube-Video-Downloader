# 🎧 YouTube Video Downloader

A Python-based command-line tool to download YouTube videos in various resolutions (360p–1080p) using the `pytube` library. It features automatic renaming based on video titles, a progress bar for downloads, and robust error handling.

## 📘 Overview

The YouTube Video Downloader simplifies the process of downloading YouTube videos by allowing users to specify a video URL and resolution from the command line. It’s an excellent showcase of real-world automation, API interaction with `pytube`, and clean error handling, making it appealing for recruiters looking for practical Python skills.

## ✨ Features

- **Resolution Selection**: Choose from available resolutions (360p, 720p, 1080p, etc.).
- **Automatic Renaming**: Saves videos with their YouTube title for easy identification.
- **Progress Bar**: Displays download progress in the terminal for a user-friendly experience.
- **Error Handling**: Gracefully handles invalid URLs, unavailable streams, and network issues.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **pytube**: For interacting with YouTube’s API to fetch and download videos.
- **argparse**: For parsing command-line arguments.
- **os**: For file handling and renaming.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- `pytube` library (`pip install pytube`)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/bnsairam/youtube-video-downloader.git
   cd youtube-video-downloader
