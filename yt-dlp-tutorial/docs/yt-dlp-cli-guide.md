# yt-dlp Complete Usage Guide

> yt-dlp is a feature-rich command-line audio/video downloader supporting thousands of websites.

## Quick Reference

| Usage | Command |
|-------|---------|
| Download video (best quality) | `yt-dlp "VIDEO_URL"` |
| Download and convert to MP3 | `yt-dlp -x --audio-format mp3 "VIDEO_URL"` |
| List available formats | `yt-dlp -F "VIDEO_URL"` |
| Download specific quality (e.g. 720p) | `yt-dlp -f "bestvideo[height<=720]+bestaudio" "VIDEO_URL"` |
| Download with subtitles | `yt-dlp --write-subs --sub-langs zh-Hans,en "VIDEO_URL"` |
| Download entire playlist | `yt-dlp "PLAYLIST_URL"` |
| Download using browser cookies | `yt-dlp --cookies-from-browser chrome "VIDEO_URL"` |
| Specify output path and filename | `yt-dlp -o "~/Downloads/%(title)s.%(ext)s" "VIDEO_URL"` |
| Update yt-dlp | `yt-dlp -U` |

## Comparison with Other Download Tools

| Feature | yt-dlp | youtube-dl (Original) | lux | BBDown |
|---------|--------|----------------------|-----|--------|
| Supported Sites | ⭐⭐⭐⭐⭐ Thousands | ⭐⭐⭐⭐ Many | ⭐⭐⭐ Moderate | ⭐ Bilibili Only |
| Update Frequency | ⭐⭐⭐⭐⭐ Very Active | ⭐ Nearly Abandoned | ⭐⭐⭐ Average | ⭐⭐⭐ Average |
| Download Speed | ⭐⭐⭐⭐⭐ Multi-threaded | ⭐⭐ Slow | ⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Fast |
| Post-processing | ⭐⭐⭐⭐⭐ Most Powerful | ⭐⭐⭐ Basic | ⭐⭐ Weak | ⭐⭐ Weak |
| Bilibili Support | ⭐⭐⭐⭐ Good | ⭐⭐ Average | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Best |

---

## 1. Installation

### macOS
```bash
# Homebrew (Recommended)
brew install yt-dlp

# pip
pip3 install -U yt-dlp

# Install ffmpeg (required for merging video/audio streams and format conversion)
brew install ffmpeg
```

### Windows
```bash
# Scoop
scoop install yt-dlp

# pip
pip install -U yt-dlp

# Or download the executable directly
# https://github.com/yt-dlp/yt-dlp/releases/latest
```

### Linux
```bash
# pip
pip3 install -U yt-dlp

# Or download the binary
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
chmod a+rx /usr/local/bin/yt-dlp
```

### Update
```bash
yt-dlp -U
```

---

## 2. Basic Usage

### 2.1 Download a Video (Default Best Quality)
```bash
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 2.2 Specify Output Path and Filename
```bash
# Save to Downloads directory with "VideoTitle.ext" naming
yt-dlp -o "~/Downloads/%(title)s.%(ext)s" "VIDEO_URL"

# Include upload date in the filename
yt-dlp -o "~/Downloads/%(upload_date)s-%(title)s.%(ext)s" "VIDEO_URL"

# Create subdirectories by channel name
yt-dlp -o "~/Downloads/%(channel)s/%(title)s.%(ext)s" "VIDEO_URL"
```

### 2.3 Common Output Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `%(title)s` | Video title | Never Gonna Give You Up |
| `%(id)s` | Video ID | dQw4w9WgXcQ |
| `%(ext)s` | File extension | mp4 |
| `%(channel)s` | Channel name | Rick Astley |
| `%(upload_date)s` | Upload date | 20091025 |
| `%(resolution)s` | Resolution | 1920x1080 |
| `%(duration)s` | Duration (seconds) | 213 |
| `%(playlist_index)s` | Playlist index | 01 |

---

## 3. Video Format Selection

### 3.1 List All Available Formats
```bash
yt-dlp -F "VIDEO_URL"
```

Sample output:
```
ID   EXT  RESOLUTION  FPS  │  FILESIZE   TBR   PROTO  │ VCODEC        ACODEC
──────────────────────────────────────────────────────────────────────────
139  m4a  audio only       │   49.84KiB  48k   https  │ audio only    mp4a.40.5
140  m4a  audio only       │  132.38KiB 128k   https  │ audio only    mp4a.40.2
137  mp4  1920x1080   25   │  305.67KiB 137k   https  │ avc1.640028   video only
248  webm 1920x1080   25   │  210.76KiB 110k   https  │ vp9           video only
```

### 3.2 Download a Specific Format
```bash
# Download by format ID (e.g. 137 from the list above)
yt-dlp -f 137 "VIDEO_URL"

# Download best video + best audio, merge automatically
yt-dlp -f "bestvideo+bestaudio/best" "VIDEO_URL"

# Download best MP4 format
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" "VIDEO_URL"
```

### 3.3 Limit Video Quality
```bash
# Max 720p
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" "VIDEO_URL"

# Max 1080p
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "VIDEO_URL"

# Max 4K
yt-dlp -f "bestvideo[height<=2160]+bestaudio/best[height<=2160]" "VIDEO_URL"
```

### 3.4 Prefer Specific Codecs
```bash
# Prefer H.264 codec (best compatibility)
yt-dlp -f "bestvideo[vcodec^=avc1]+bestaudio/best" "VIDEO_URL"

# Prefer VP9 codec (smaller file size)
yt-dlp -f "bestvideo[vcodec^=vp9]+bestaudio/best" "VIDEO_URL"
```

### 3.5 Format Sorting (Advanced)
```bash
# Prioritize: resolution > codec > file size
yt-dlp -S "res,codec,filesize" "VIDEO_URL"

# Prefer the highest quality with H.264 codec
yt-dlp -S "codec:h264" "VIDEO_URL"
```

---

## 4. Audio Download

### 4.1 Extract Audio Only
```bash
# Extract audio in default format
yt-dlp -x "VIDEO_URL"

# Extract audio and convert to MP3
yt-dlp -x --audio-format mp3 "VIDEO_URL"

# Extract audio and convert to FLAC (lossless)
yt-dlp -x --audio-format flac "VIDEO_URL"

# Specify audio quality (0 = best, 10 = worst)
yt-dlp -x --audio-format mp3 --audio-quality 0 "VIDEO_URL"
```

### 4.2 Supported Audio Formats
`mp3` / `aac` / `flac` / `m4a` / `opus` / `vorbis` / `wav`

---

## 5. Subtitle Download

### 5.1 Download Subtitles
```bash
# Download all available subtitles
yt-dlp --write-subs "VIDEO_URL"

# Download subtitles for specific languages (Chinese and English)
yt-dlp --write-subs --sub-langs "zh-Hans,en" "VIDEO_URL"

# Download auto-generated subtitles
yt-dlp --write-auto-subs --sub-langs "zh-Hans" "VIDEO_URL"

# Download subtitles only (skip video download)
yt-dlp --write-subs --sub-langs "zh-Hans,en" --skip-download "VIDEO_URL"
```

### 5.2 Convert Subtitle Format
```bash
# Convert to SRT format
yt-dlp --write-subs --sub-format srt --convert-subs srt "VIDEO_URL"
```

### 5.3 Embed Subtitles into Video
```bash
yt-dlp --write-subs --sub-langs "zh-Hans,en" --embed-subs "VIDEO_URL"
```

---

## 6. Playlist Handling

### 6.1 Download an Entire Playlist
```bash
yt-dlp "https://www.youtube.com/playlist?list=PLxxxxxx"
```

### 6.2 Specify Download Range
```bash
# Download only items 3 through 7
yt-dlp --playlist-start 3 --playlist-end 7 "PLAYLIST_URL"

# Download only items 1, 3, and 5
yt-dlp --playlist-items 1,3,5 "PLAYLIST_URL"

# Download items 1 to 10, every other item
yt-dlp --playlist-items 1:10:2 "PLAYLIST_URL"
```

### 6.3 Numbered Filenames for Playlists
```bash
# Filenames with index, e.g. "01-Title.mp4"
yt-dlp -o "%(playlist_index)02d-%(title)s.%(ext)s" "PLAYLIST_URL"
```

### 6.4 Disable Playlist Download (Single Video Only)
```bash
yt-dlp --no-playlist "VIDEO_URL"
```

---

## 7. Download Limits & Controls

### 7.1 Rate Limiting
```bash
# Limit to 1MB/s
yt-dlp -r 1M "VIDEO_URL"

# Limit to 500KB/s
yt-dlp -r 500K "VIDEO_URL"
```

### 7.2 File Size Limit
```bash
# Only download formats smaller than 100MB
yt-dlp -f "best[filesize<100M]" "VIDEO_URL"
```

### 7.3 Retries & Timeout
```bash
# Retry up to 10 times
yt-dlp --retries 10 "VIDEO_URL"

# Set connection timeout to 30 seconds
yt-dlp --socket-timeout 30 "VIDEO_URL"

# Set fragment retries
yt-dlp --fragment-retries 10 "VIDEO_URL"
```

### 7.4 Resume Interrupted Downloads
```bash
# Continue a previously interrupted download
yt-dlp -c "VIDEO_URL"
```

### 7.5 Skip Already Downloaded Files
```bash
# Use a download archive to avoid re-downloading
yt-dlp --download-archive downloaded.txt "VIDEO_URL"
```

### 7.6 Proxy Configuration
```bash
# HTTP proxy
yt-dlp --proxy http://127.0.0.1:7890 "VIDEO_URL"

# SOCKS5 proxy
yt-dlp --proxy socks5://127.0.0.1:1080 "VIDEO_URL"
```

---

## 8. Cookies & Authentication

### 8.1 Auto-extract Cookies from Browser
```bash
# Chrome
yt-dlp --cookies-from-browser chrome "VIDEO_URL"

# Safari
yt-dlp --cookies-from-browser safari "VIDEO_URL"

# Edge
yt-dlp --cookies-from-browser edge "VIDEO_URL"

# Firefox
yt-dlp --cookies-from-browser firefox "VIDEO_URL"
```

### 8.2 Use a Cookie File
```bash
yt-dlp --cookies cookies.txt "VIDEO_URL"
```

### 8.3 Username & Password Login
```bash
yt-dlp -u USERNAME -p PASSWORD "VIDEO_URL"
```

---

## 9. Post-processing

### 9.1 Embed Metadata
```bash
# Embed thumbnail
yt-dlp --embed-thumbnail "VIDEO_URL"

# Embed metadata (title, description, date, etc.)
yt-dlp --embed-metadata "VIDEO_URL"

# Embed chapter information
yt-dlp --embed-chapters "VIDEO_URL"

# Embed all metadata at once
yt-dlp --embed-thumbnail --embed-metadata --embed-chapters --embed-subs "VIDEO_URL"
```

### 9.2 Video Conversion
```bash
# Remux to MP4 container (no re-encoding, fast)
yt-dlp --remux-video mp4 "VIDEO_URL"

# Re-encode to MP4 (slower, ensures compatibility)
yt-dlp --recode-video mp4 "VIDEO_URL"
```

### 9.3 SponsorBlock (Skip Sponsored Segments)
```bash
# Remove sponsor segments
yt-dlp --sponsorblock-remove sponsor "VIDEO_URL"

# Remove all non-content segments
yt-dlp --sponsorblock-remove all "VIDEO_URL"

# Mark sponsor segments as chapters (without removing)
yt-dlp --sponsorblock-mark sponsor "VIDEO_URL"
```

### 9.4 Download Specific Time Range
```bash
# Download from 0:30 to 2:00
yt-dlp --download-sections "*00:00:30-00:02:00" "VIDEO_URL"

# Download the first 60 seconds
yt-dlp --download-sections "*00:00:00-00:01:00" "VIDEO_URL"
```

---

## 10. Bilibili-specific Tips

### 10.1 Basic Download
```bash
yt-dlp "https://www.bilibili.com/video/BVxxxxxxxx"
```

### 10.2 Download with Cookies (Fix HTTP 403 Error)
```bash
yt-dlp --cookies-from-browser chrome "https://www.bilibili.com/video/BVxxxxxxxx"
```

### 10.3 Download Highest Quality
```bash
yt-dlp --cookies-from-browser chrome -f "bestvideo+bestaudio/best" "BILIBILI_URL"
```

### 10.4 Download Multi-part Videos / Collections
```bash
# Download all parts
yt-dlp --cookies-from-browser chrome "BILIBILI_URL"

# Download only parts 1 through 5
yt-dlp --cookies-from-browser chrome --playlist-items 1-5 "BILIBILI_URL"
```

---

## 11. Configuration File

Frequently used options can be saved in a configuration file to avoid repetitive typing.

### Config File Locations
- **macOS/Linux**: `~/.config/yt-dlp/config`
- **Windows**: `%APPDATA%\yt-dlp\config`

### Example Configuration
```ini
# Default output path
-o ~/Downloads/yt-dlp/%(channel)s/%(title)s.%(ext)s

# Default best quality (max 1080p)
-f bestvideo[height<=1080]+bestaudio/best[height<=1080]

# Embed metadata and thumbnail
--embed-metadata
--embed-thumbnail

# Use download archive to avoid re-downloading
--download-archive ~/Downloads/yt-dlp/archive.txt

# Use Chrome cookies
--cookies-from-browser chrome

# Rate limit to 5MB/s
-r 5M
```

---

## 12. Practical Combined Commands

```bash
# Perfect download: 1080p + embedded subtitles/thumbnail/metadata
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best" \
  --embed-subs --write-auto-subs --sub-langs "zh-Hans,en" \
  --embed-thumbnail --embed-metadata --embed-chapters \
  -o "~/Downloads/%(title)s.%(ext)s" "VIDEO_URL"

# Batch download a music playlist as MP3
yt-dlp -x --audio-format mp3 --audio-quality 0 \
  --embed-thumbnail --embed-metadata \
  -o "~/Music/%(playlist_index)02d-%(title)s.%(ext)s" "PLAYLIST_URL"

# Download the latest 10 videos from a channel
yt-dlp --playlist-end 10 \
  -o "~/Downloads/%(channel)s/%(upload_date)s-%(title)s.%(ext)s" \
  "https://www.youtube.com/@CHANNEL_NAME/videos"

# Dump video metadata as JSON (no download)
yt-dlp --dump-json "VIDEO_URL" | python3 -m json.tool
```
