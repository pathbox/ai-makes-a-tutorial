#!/usr/bin/env python3
"""
yt-dlp Python 调用完整示例
============================

功能：
1. 基础视频下载（支持多种格式和画质）
2. 音频提取（MP3/FLAC）
3. 播放列表批量下载
4. 字幕下载与嵌入
5. 错误日志捕获与处理
6. 异步批量下载任务
7. 下载进度回调与监控
8. 配置管理（可扩展）

依赖：pip install yt-dlp
"""

import asyncio
import json
import logging
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import yt_dlp

# ============================================================
# 日志配置
# ============================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "yt-dlp.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("yt-dlp-demo")


# ============================================================
# 配置数据类
# ============================================================

class Quality(Enum):
    """视频画质枚举"""
    BEST = "bestvideo+bestaudio/best"
    P2160 = "bestvideo[height<=2160]+bestaudio/best[height<=2160]"
    P1080 = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    P720 = "bestvideo[height<=720]+bestaudio/best[height<=720]"
    P480 = "bestvideo[height<=480]+bestaudio/best[height<=480]"
    AUDIO_ONLY = "bestaudio/best"


class AudioFormat(Enum):
    """音频格式枚举"""
    MP3 = "mp3"
    FLAC = "flac"
    M4A = "m4a"
    WAV = "wav"
    OPUS = "opus"


@dataclass
class DownloadConfig:
    """下载配置"""
    # 基础配置
    output_dir: str = "./downloads"
    filename_template: str = "%(title)s.%(ext)s"
    quality: Quality = Quality.P1080

    # 网络配置
    proxy: Optional[str] = None
    rate_limit: Optional[str] = None  # 如 "1M", "500K"
    retries: int = 5
    socket_timeout: int = 30

    # Cookie 配置
    cookies_from_browser: Optional[str] = None  # "chrome", "safari", "edge"
    cookies_file: Optional[str] = None

    # 字幕配置
    write_subs: bool = False
    sub_langs: str = "zh-Hans,en"
    embed_subs: bool = False
    auto_subs: bool = False

    # 嵌入配置
    embed_thumbnail: bool = False
    embed_metadata: bool = False
    embed_chapters: bool = False

    # 播放列表配置
    playlist_start: Optional[int] = None
    playlist_end: Optional[int] = None
    playlist_items: Optional[str] = None
    no_playlist: bool = False

    # 音频提取
    extract_audio: bool = False
    audio_format: AudioFormat = AudioFormat.MP3
    audio_quality: int = 0  # 0=最佳 10=最差

    # 下载归档（避免重复下载）
    download_archive: Optional[str] = None

    # 并发配置
    max_workers: int = 3

    def to_yt_dlp_opts(self) -> dict:
        """转换为 yt-dlp 参数字典"""
        output_path = os.path.join(self.output_dir, self.filename_template)

        opts = {
            "outtmpl": output_path,
            "format": self.quality.value,
            "retries": self.retries,
            "socket_timeout": self.socket_timeout,
            "ignoreerrors": True,
            "no_warnings": False,
            "noprogress": False,
        }

        # 网络
        if self.proxy:
            opts["proxy"] = self.proxy
        if self.rate_limit:
            opts["ratelimit"] = self._parse_rate(self.rate_limit)

        # Cookie
        if self.cookies_from_browser:
            opts["cookiesfrombrowser"] = (self.cookies_from_browser,)
        if self.cookies_file:
            opts["cookiefile"] = self.cookies_file

        # 字幕
        if self.write_subs or self.auto_subs:
            opts["writesubtitles"] = self.write_subs
            opts["writeautomaticsub"] = self.auto_subs
            opts["subtitleslangs"] = self.sub_langs.split(",")

        # 播放列表
        if self.no_playlist:
            opts["noplaylist"] = True
        if self.playlist_start:
            opts["playliststart"] = self.playlist_start
        if self.playlist_end:
            opts["playlistend"] = self.playlist_end
        if self.playlist_items:
            opts["playlist_items"] = self.playlist_items

        # 下载归档
        if self.download_archive:
            opts["download_archive"] = self.download_archive

        # 后处理器
        postprocessors = []
        if self.extract_audio:
            opts["format"] = Quality.AUDIO_ONLY.value
            postprocessors.append({
                "key": "FFmpegExtractAudio",
                "preferredcodec": self.audio_format.value,
                "preferredquality": str(self.audio_quality),
            })
        if self.embed_thumbnail:
            postprocessors.append({"key": "EmbedThumbnail"})
            opts["writethumbnail"] = True
        if self.embed_metadata:
            postprocessors.append({"key": "FFmpegMetadata"})
        if self.embed_subs:
            postprocessors.append({"key": "FFmpegEmbedSubtitle"})
        if self.embed_chapters:
            postprocessors.append({"key": "FFmpegEmbedChapters"})

        if postprocessors:
            opts["postprocessors"] = postprocessors

        return opts

    @staticmethod
    def _parse_rate(rate: str) -> int:
        """解析限速字符串（如 '1M' -> 1048576）"""
        rate = rate.strip().upper()
        if rate.endswith("M"):
            return int(float(rate[:-1]) * 1024 * 1024)
        elif rate.endswith("K"):
            return int(float(rate[:-1]) * 1024)
        return int(rate)


# ============================================================
# 进度钩子（回调）
# ============================================================

class ProgressHook:
    """下载进度回调处理器"""

    def __init__(self):
        self.start_time = None
        self.downloads: list[dict] = []

    def __call__(self, d: dict):
        status = d.get("status")

        if status == "downloading":
            if self.start_time is None:
                self.start_time = time.time()

            total = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
            downloaded = d.get("downloaded_bytes", 0)
            speed = d.get("speed", 0)
            eta = d.get("eta", 0)

            if total > 0:
                percent = downloaded / total * 100
                total_mb = total / 1024 / 1024
                down_mb = downloaded / 1024 / 1024
                speed_mb = (speed or 0) / 1024 / 1024

                print(
                    f"\r  ⬇️  {percent:5.1f}% | "
                    f"{down_mb:.1f}/{total_mb:.1f} MB | "
                    f"{speed_mb:.2f} MB/s | "
                    f"ETA: {eta or '?'}s",
                    end="", flush=True,
                )

        elif status == "finished":
            elapsed = time.time() - (self.start_time or time.time())
            filename = d.get("filename", "unknown")
            filesize = d.get("total_bytes", 0) / 1024 / 1024

            print(f"\n  ✅ 下载完成: {os.path.basename(filename)} ({filesize:.1f} MB, 耗时 {elapsed:.1f}s)")
            logger.info(f"下载完成: {filename} ({filesize:.1f} MB)")

            self.downloads.append({
                "filename": filename,
                "filesize_mb": round(filesize, 1),
                "elapsed_seconds": round(elapsed, 1),
            })
            self.start_time = None

        elif status == "error":
            print(f"\n  ❌ 下载出错")
            logger.error(f"下载出错: {d}")


# ============================================================
# 自定义日志处理器
# ============================================================

class YtDlpLogger:
    """yt-dlp 日志适配器，将日志输出到 Python logging"""

    def debug(self, msg):
        if msg.startswith("[debug]"):
            logger.debug(msg)
        else:
            logger.info(msg)

    def info(self, msg):
        logger.info(msg)

    def warning(self, msg):
        logger.warning(msg)

    def error(self, msg):
        logger.error(msg)


# ============================================================
# 核心下载器类
# ============================================================

class VideoDownloader:
    """视频下载器核心类"""

    def __init__(self, config: Optional[DownloadConfig] = None):
        self.config = config or DownloadConfig()
        self.progress_hook = ProgressHook()
        os.makedirs(self.config.output_dir, exist_ok=True)

    def _build_opts(self, **overrides) -> dict:
        """构建 yt-dlp 参数"""
        opts = self.config.to_yt_dlp_opts()
        opts["logger"] = YtDlpLogger()
        opts["progress_hooks"] = [self.progress_hook]
        opts.update(overrides)
        return opts

    # ------ 信息获取 ------

    def get_info(self, url: str) -> Optional[dict]:
        """获取视频信息（不下载）"""
        opts = self._build_opts()
        opts["skip_download"] = True
        opts["quiet"] = True

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            logger.error(f"获取信息失败 [{url}]: {e}")
            return None

    def list_formats(self, url: str):
        """列出视频可用格式"""
        info = self.get_info(url)
        if not info:
            print("❌ 无法获取视频信息")
            return

        print(f"\n📹 {info.get('title', 'Unknown')}")
        print(f"   时长: {info.get('duration', '?')}s | 频道: {info.get('channel', '?')}")
        print(f"\n{'ID':<8} {'EXT':<6} {'分辨率':<12} {'大小':<12} {'编码':<15} {'备注'}")
        print("-" * 70)

        for f in info.get("formats", []):
            fid = f.get("format_id", "?")
            ext = f.get("ext", "?")
            res = f.get("resolution", "audio only")
            size = f.get("filesize") or f.get("filesize_approx", 0)
            size_str = f"{size / 1024 / 1024:.1f}MB" if size else "?"
            vcodec = f.get("vcodec", "none")
            acodec = f.get("acodec", "none")
            note = f.get("format_note", "")

            codec = vcodec if vcodec != "none" else acodec
            print(f"{fid:<8} {ext:<6} {res:<12} {size_str:<12} {codec:<15} {note}")

    # ------ 下载方法 ------

    def download(self, url: str, **overrides) -> bool:
        """下载单个视频"""
        opts = self._build_opts(**overrides)
        logger.info(f"开始下载: {url}")
        print(f"\n🎬 开始下载: {url}")

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            return True
        except yt_dlp.utils.DownloadError as e:
            logger.error(f"下载失败 [{url}]: {e}")
            print(f"❌ 下载失败: {e}")
            return False
        except Exception as e:
            logger.error(f"未知错误 [{url}]: {e}")
            print(f"❌ 未知错误: {e}")
            return False

    def download_audio(self, url: str, fmt: AudioFormat = AudioFormat.MP3) -> bool:
        """下载音频"""
        overrides = {
            "format": Quality.AUDIO_ONLY.value,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": fmt.value,
                "preferredquality": "0",
            }],
        }
        logger.info(f"开始下载音频 [{fmt.value}]: {url}")
        print(f"\n🎵 开始下载音频 ({fmt.value}): {url}")
        return self.download(url, **overrides)

    def download_with_subs(self, url: str, langs: str = "zh-Hans,en") -> bool:
        """下载视频并嵌入字幕"""
        overrides = {
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": langs.split(","),
            "postprocessors": [
                {"key": "FFmpegEmbedSubtitle"},
                {"key": "FFmpegMetadata"},
            ],
        }
        logger.info(f"开始下载（含字幕）: {url}")
        print(f"\n📝 开始下载（含字幕）: {url}")
        return self.download(url, **overrides)

    def download_playlist(
        self,
        url: str,
        start: Optional[int] = None,
        end: Optional[int] = None,
        items: Optional[str] = None,
    ) -> bool:
        """下载播放列表"""
        overrides = {
            "outtmpl": os.path.join(
                self.config.output_dir,
                "%(playlist_title)s",
                "%(playlist_index)03d-%(title)s.%(ext)s",
            ),
        }
        if start:
            overrides["playliststart"] = start
        if end:
            overrides["playlistend"] = end
        if items:
            overrides["playlist_items"] = items

        logger.info(f"开始下载播放列表: {url}")
        print(f"\n📋 开始下载播放列表: {url}")
        return self.download(url, **overrides)

    # ------ 批量同步下载 ------

    def batch_download(self, urls: list[str]) -> dict:
        """批量下载多个视频"""
        results = {"success": [], "failed": []}
        total = len(urls)

        for i, url in enumerate(urls, 1):
            print(f"\n{'='*50}")
            print(f"📦 批量下载 [{i}/{total}]")
            print(f"{'='*50}")

            if self.download(url):
                results["success"].append(url)
            else:
                results["failed"].append(url)

        print(f"\n{'='*50}")
        print(f"📊 批量下载完成: ✅ {len(results['success'])} 成功 / ❌ {len(results['failed'])} 失败")
        print(f"{'='*50}")
        return results


# ============================================================
# 异步下载器（基于线程池）
# ============================================================

class AsyncDownloader:
    """异步批量下载器"""

    def __init__(self, config: Optional[DownloadConfig] = None):
        self.config = config or DownloadConfig()

    def _download_single(self, url: str) -> dict:
        """单个下载任务（在线程中执行）"""
        downloader = VideoDownloader(self.config)
        start = time.time()
        success = downloader.download(url)
        elapsed = time.time() - start

        return {
            "url": url,
            "success": success,
            "elapsed": round(elapsed, 1),
            "files": downloader.progress_hook.downloads,
        }

    async def download_batch(self, urls: list[str]) -> list[dict]:
        """异步批量下载"""
        max_workers = min(self.config.max_workers, len(urls))
        logger.info(f"异步批量下载: {len(urls)} 个任务, {max_workers} 并发")
        print(f"\n🚀 启动异步批量下载: {len(urls)} 个任务, {max_workers} 并发")

        loop = asyncio.get_event_loop()
        results = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            tasks = [
                loop.run_in_executor(executor, self._download_single, url)
                for url in urls
            ]
            results = await asyncio.gather(*tasks, return_exceptions=True)

        # 统计结果
        success_count = sum(1 for r in results if isinstance(r, dict) and r.get("success"))
        fail_count = len(results) - success_count

        print(f"\n{'='*50}")
        print(f"📊 异步下载完成: ✅ {success_count} 成功 / ❌ {fail_count} 失败")
        for r in results:
            if isinstance(r, dict):
                status = "✅" if r["success"] else "❌"
                print(f"   {status} {r['url']} ({r['elapsed']}s)")
            else:
                print(f"   ❌ 异常: {r}")
        print(f"{'='*50}")

        return results


# ============================================================
# 使用示例
# ============================================================

def example_basic_download():
    """示例 1：基础视频下载"""
    config = DownloadConfig(
        output_dir="./downloads/videos",
        quality=Quality.P1080,
    )
    dl = VideoDownloader(config)
    dl.download("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def example_audio_download():
    """示例 2：下载音频（MP3）"""
    config = DownloadConfig(output_dir="./downloads/music")
    dl = VideoDownloader(config)
    dl.download_audio(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        fmt=AudioFormat.MP3,
    )


def example_with_subs():
    """示例 3：下载视频并嵌入中英文字幕"""
    config = DownloadConfig(
        output_dir="./downloads/with-subs",
        quality=Quality.P1080,
    )
    dl = VideoDownloader(config)
    dl.download_with_subs(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        langs="zh-Hans,en",
    )


def example_playlist():
    """示例 4：下载播放列表（第 1-5 个视频）"""
    config = DownloadConfig(
        output_dir="./downloads/playlist",
        quality=Quality.P720,
    )
    dl = VideoDownloader(config)
    dl.download_playlist(
        "https://www.youtube.com/playlist?list=PLxxxxxx",
        start=1,
        end=5,
    )


def example_bilibili():
    """示例 5：下载 B 站视频（带 Cookie）"""
    config = DownloadConfig(
        output_dir="./downloads/bilibili",
        quality=Quality.P1080,
        cookies_from_browser="chrome",
    )
    dl = VideoDownloader(config)
    dl.download("https://www.bilibili.com/video/BVxxxxxxxx")


def example_batch():
    """示例 6：批量同步下载"""
    config = DownloadConfig(
        output_dir="./downloads/batch",
        quality=Quality.P720,
    )
    dl = VideoDownloader(config)

    urls = [
        "https://www.youtube.com/watch?v=video1",
        "https://www.youtube.com/watch?v=video2",
        "https://www.youtube.com/watch?v=video3",
    ]
    results = dl.batch_download(urls)
    print(json.dumps(results, indent=2, ensure_ascii=False))


async def example_async_batch():
    """示例 7：异步并发下载"""
    config = DownloadConfig(
        output_dir="./downloads/async",
        quality=Quality.P720,
        max_workers=3,
    )
    dl = AsyncDownloader(config)

    urls = [
        "https://www.youtube.com/watch?v=video1",
        "https://www.youtube.com/watch?v=video2",
        "https://www.youtube.com/watch?v=video3",
    ]
    results = await dl.download_batch(urls)
    return results


def example_list_formats():
    """示例 8：查看视频可用格式"""
    dl = VideoDownloader()
    dl.list_formats("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def example_full_config():
    """示例 9：完整配置演示"""
    config = DownloadConfig(
        # 保存配置
        output_dir="./downloads/full",
        filename_template="%(channel)s/%(upload_date)s-%(title)s.%(ext)s",
        quality=Quality.P1080,

        # 网络配置
        proxy="socks5://127.0.0.1:1080",
        rate_limit="5M",
        retries=10,

        # Cookie
        cookies_from_browser="chrome",

        # 字幕
        write_subs=True,
        auto_subs=True,
        sub_langs="zh-Hans,en",
        embed_subs=True,

        # 嵌入元数据
        embed_thumbnail=True,
        embed_metadata=True,
        embed_chapters=True,

        # 下载归档
        download_archive="./downloads/archive.txt",
    )

    dl = VideoDownloader(config)
    dl.download("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# ============================================================
# 主函数
# ============================================================

def main():
    """主入口：选择运行示例"""
    examples = {
        "1": ("基础视频下载", example_basic_download),
        "2": ("下载音频 (MP3)", example_audio_download),
        "3": ("下载视频 + 字幕", example_with_subs),
        "4": ("下载播放列表", example_playlist),
        "5": ("下载 B 站视频", example_bilibili),
        "6": ("批量同步下载", example_batch),
        "7": ("异步并发下载", lambda: asyncio.run(example_async_batch())),
        "8": ("查看视频格式", example_list_formats),
        "9": ("完整配置演示", example_full_config),
    }

    print("\n" + "=" * 50)
    print("  yt-dlp Python 调用示例")
    print("=" * 50)
    for key, (name, _) in examples.items():
        print(f"  [{key}] {name}")
    print("  [q] 退出")
    print("=" * 50)

    choice = input("\n请选择示例编号: ").strip()

    if choice == "q":
        print("再见！")
        return

    if choice in examples:
        name, func = examples[choice]
        print(f"\n▶ 运行示例: {name}")
        print("-" * 50)
        func()
    else:
        print("❌ 无效选择")


if __name__ == "__main__":
    main()
