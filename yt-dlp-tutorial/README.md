# yt-dlp 完整使用教程 & Python 示例

一个包含 **命令行教程** 和 **Python 调用示例** 的 yt-dlp 完整学习项目。

## 📁 项目结构

```
yt-dlp-tutorial/
├── README.md                          # 本文件
├── requirements.txt                   # Python 依赖
├── yt_dlp_demo.py                     # Python 完整示例代码
├── docs/
│   └── yt-dlp-命令行教程.md            # 命令行使用详细教程
    └── yt-dlp-guide.md               # 命令行使用详细教程
├── downloads/                         # 下载文件保存目录（自动创建）
└── logs/                              # 日志目录（自动创建）
    └── yt-dlp.log
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 安装 yt-dlp
pip3 install -r requirements.txt

# 安装 ffmpeg（视频合并、音频转换必备）
brew install ffmpeg    # macOS
```

### 2. 命令行使用

```bash
# 下载视频
yt-dlp "https://www.youtube.com/watch?v=视频ID"

# 下载音频
yt-dlp -x --audio-format mp3 "视频链接"

# 更多用法请查看 docs/yt-dlp-命令行教程.md
```

### 3. Python 调用

```bash
python3 yt_dlp_demo.py
```

运行后会显示交互菜单，可选择不同的下载示例。

## 📖 文档

- **[命令行教程](docs/yt-dlp-命令行教程.md)** — 涵盖格式选择、画质限制、字幕下载、播放列表、Cookie 登录、后处理等
- **[yt_dlp_demo.py](yt_dlp_demo.py)** — Python 代码示例，包含：
  - `DownloadConfig` — 可扩展的配置数据类
  - `VideoDownloader` — 同步下载器（支持视频/音频/字幕/播放列表）
  - `AsyncDownloader` — 异步并发下载器（基于线程池）
  - `ProgressHook` — 下载进度回调监控
  - `YtDlpLogger` — 日志捕获与记录

## 🔧 Python 代码快速使用

```python
from yt_dlp_demo import VideoDownloader, DownloadConfig, Quality, AudioFormat

# 下载 1080p 视频
config = DownloadConfig(output_dir="./my_videos", quality=Quality.P1080)
dl = VideoDownloader(config)
dl.download("https://www.youtube.com/watch?v=xxxxx")

# 下载 MP3 音频
dl.download_audio("https://www.youtube.com/watch?v=xxxxx", fmt=AudioFormat.MP3)

# 异步批量下载
import asyncio
from yt_dlp_demo import AsyncDownloader

async def main():
    dl = AsyncDownloader(DownloadConfig(max_workers=3))
    await dl.download_batch(["url1", "url2", "url3"])

asyncio.run(main())
```

## ⚠️ 注意事项

- 下载 B 站视频需要带 Cookie：设置 `cookies_from_browser="chrome"`
- 音频转换和视频合并需要安装 **ffmpeg**
- 使用代理：设置 `proxy="socks5://127.0.0.1:1080"`
- 日志文件保存在 `logs/yt-dlp.log`
