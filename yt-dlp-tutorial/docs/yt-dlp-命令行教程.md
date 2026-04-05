# yt-dlp 完整使用教程

> yt-dlp 是一个功能丰富的命令行音频/视频下载工具，支持数千个网站。

## 常用命令速查

|用途	|命令|
|------|------|
|下载视频（最佳画质）	|yt-dlp "视频链接"|
|下载并转为| MP3	yt-dlp -x --audio-format mp3 "视频链接"|
|查看可用画质列表|	yt-dlp -F "视频链接"|
|下载指定画质（如 720p）|	yt-dlp -f "bestvideo[height<=720]+bestaudio" "视频链接"|
|下载带字幕	|yt-dlp --write-subs --sub-langs zh-Hans,en "视频链接"|
|下载整个播放列表|	yt-dlp "播放列表链接"|
|用浏览器 Cookie 下载|	yt-dlp --cookies-from-browser chrome "视频链接"|
|指定保存路径和文件名|	yt-dlp -o "~/Downloads/%(title)s.%(ext)s" "视频链接"|
|更新 yt-dlp|	yt-dlp -U|

## 与其他下载工具对比

| 特性 | yt-dlp | youtube-dl（原版） | lux | BBDown |
|------|--------|-------------------|-----|--------|
| 支持网站数量 | ⭐⭐⭐⭐⭐ 几千个 | ⭐⭐⭐⭐ 多 | ⭐⭐⭐ 中等 | ⭐ B站专用 |
| 更新频率 | ⭐⭐⭐⭐⭐ 非常活跃 | ⭐ 几乎停更 | ⭐⭐⭐ 一般 | ⭐⭐⭐ 一般 |
| 下载速度 | ⭐⭐⭐⭐⭐ 多线程 | ⭐⭐ 慢 | ⭐⭐⭐⭐ 快 | ⭐⭐⭐⭐ 快 |
| 后处理能力 | ⭐⭐⭐⭐⭐ 最强 | ⭐⭐⭐ 基础 | ⭐⭐ 弱 | ⭐⭐ 弱 |
| B 站支持 | ⭐⭐⭐⭐ 好 | ⭐⭐ 一般 | ⭐⭐⭐⭐ 好 | ⭐⭐⭐⭐⭐ 最好 |

---

## 一、安装

### macOS
```bash
# Homebrew（推荐）
brew install yt-dlp

# pip
pip3 install -U yt-dlp

# 同时安装 ffmpeg（合并视频音频、转格式必备）
brew install ffmpeg
```

### Windows
```bash
# Scoop
scoop install yt-dlp

# pip
pip install -U yt-dlp

# 或直接下载 exe
# https://github.com/yt-dlp/yt-dlp/releases/latest
```

### Linux
```bash
# pip
pip3 install -U yt-dlp

# 或下载二进制
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
chmod a+rx /usr/local/bin/yt-dlp
```

### 更新
```bash
yt-dlp -U
```

---

## 二、基础用法

### 2.1 直接下载（默认最佳画质）
```bash
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 2.2 指定保存路径和文件名
```bash
# 保存到 Downloads 目录，文件名为 "视频标题.扩展名"
yt-dlp -o "~/Downloads/%(title)s.%(ext)s" "视频链接"

# 带上传日期的文件名
yt-dlp -o "~/Downloads/%(upload_date)s-%(title)s.%(ext)s" "视频链接"

# 按频道名创建子文件夹
yt-dlp -o "~/Downloads/%(channel)s/%(title)s.%(ext)s" "视频链接"
```

### 2.3 常用文件名模板变量

| 变量 | 说明 | 示例 |
|------|------|------|
| `%(title)s` | 视频标题 | Never Gonna Give You Up |
| `%(id)s` | 视频 ID | dQw4w9WgXcQ |
| `%(ext)s` | 文件扩展名 | mp4 |
| `%(channel)s` | 频道名 | Rick Astley |
| `%(upload_date)s` | 上传日期 | 20091025 |
| `%(resolution)s` | 分辨率 | 1920x1080 |
| `%(duration)s` | 时长（秒） | 213 |
| `%(playlist_index)s` | 播放列表序号 | 01 |

---

## 三、视频格式选择

### 3.1 查看所有可用格式
```bash
yt-dlp -F "视频链接"
```

输出示例：
```
ID   EXT  RESOLUTION  FPS  │  FILESIZE   TBR   PROTO  │ VCODEC        ACODEC
──────────────────────────────────────────────────────────────────────────
139  m4a  audio only       │   49.84KiB  48k   https  │ audio only    mp4a.40.5
140  m4a  audio only       │  132.38KiB 128k   https  │ audio only    mp4a.40.2
137  mp4  1920x1080   25   │  305.67KiB 137k   https  │ avc1.640028   video only
248  webm 1920x1080   25   │  210.76KiB 110k   https  │ vp9           video only
```

### 3.2 下载指定格式
```bash
# 下载指定 format ID（如上面的 137）
yt-dlp -f 137 "视频链接"

# 下载最佳视频 + 最佳音频，自动合并
yt-dlp -f "bestvideo+bestaudio/best" "视频链接"

# 下载最佳 mp4 格式
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" "视频链接"
```

### 3.3 限制画质
```bash
# 最高 720p
yt-dlp -f "bestvideo[height<=720]+bestaudio/best[height<=720]" "视频链接"

# 最高 1080p
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "视频链接"

# 最高 4K
yt-dlp -f "bestvideo[height<=2160]+bestaudio/best[height<=2160]" "视频链接"
```

### 3.4 优先选择特定编码
```bash
# 优先 h264 编码（兼容性最好）
yt-dlp -f "bestvideo[vcodec^=avc1]+bestaudio/best" "视频链接"

# 优先 VP9 编码（体积更小）
yt-dlp -f "bestvideo[vcodec^=vp9]+bestaudio/best" "视频链接"
```

### 3.5 格式排序（高级）
```bash
# 优先选择：分辨率 > 编码 > 文件大小
yt-dlp -S "res,codec,filesize" "视频链接"

# 优先选择 h264 编码的最高画质
yt-dlp -S "codec:h264" "视频链接"
```

---

## 四、音频下载

### 4.1 只下载音频
```bash
# 提取音频，默认格式
yt-dlp -x "视频链接"

# 提取音频并转为 MP3
yt-dlp -x --audio-format mp3 "视频链接"

# 提取音频并转为 FLAC（无损）
yt-dlp -x --audio-format flac "视频链接"

# 指定音频质量（0=最佳，10=最差）
yt-dlp -x --audio-format mp3 --audio-quality 0 "视频链接"
```

### 4.2 支持的音频格式
`mp3` / `aac` / `flac` / `m4a` / `opus` / `vorbis` / `wav`

---

## 五、字幕下载

### 5.1 下载字幕
```bash
# 下载所有可用字幕
yt-dlp --write-subs "视频链接"

# 下载指定语言字幕（中文和英文）
yt-dlp --write-subs --sub-langs "zh-Hans,en" "视频链接"

# 下载自动生成的字幕
yt-dlp --write-auto-subs --sub-langs "zh-Hans" "视频链接"

# 只下载字幕，不下载视频
yt-dlp --write-subs --sub-langs "zh-Hans,en" --skip-download "视频链接"
```

### 5.2 字幕格式转换
```bash
# 转换为 SRT 格式
yt-dlp --write-subs --sub-format srt --convert-subs srt "视频链接"
```

### 5.3 嵌入字幕到视频
```bash
yt-dlp --write-subs --sub-langs "zh-Hans,en" --embed-subs "视频链接"
```

---

## 六、播放列表处理

### 6.1 下载整个播放列表
```bash
yt-dlp "https://www.youtube.com/playlist?list=PLxxxxxx"
```

### 6.2 指定下载范围
```bash
# 只下载第 3 到第 7 个视频
yt-dlp --playlist-start 3 --playlist-end 7 "播放列表链接"

# 只下载第 1、3、5 个
yt-dlp --playlist-items 1,3,5 "播放列表链接"

# 下载第 1 到第 10 个，每隔一个下载
yt-dlp --playlist-items 1:10:2 "播放列表链接"
```

### 6.3 播放列表文件名编号
```bash
# 文件名带序号，如 "01-标题.mp4"
yt-dlp -o "%(playlist_index)02d-%(title)s.%(ext)s" "播放列表链接"
```

### 6.4 不下载播放列表（只下载单个视频）
```bash
yt-dlp --no-playlist "视频链接"
```

---

## 七、下载限制与控制

### 7.1 限速
```bash
# 限速 1MB/s
yt-dlp -r 1M "视频链接"

# 限速 500KB/s
yt-dlp -r 500K "视频链接"
```

### 7.2 限制文件大小
```bash
# 只下载小于 100MB 的格式
yt-dlp -f "best[filesize<100M]" "视频链接"
```

### 7.3 重试与超时
```bash
# 重试 10 次
yt-dlp --retries 10 "视频链接"

# 设置连接超时 30 秒
yt-dlp --socket-timeout 30 "视频链接"

# 分片重试
yt-dlp --fragment-retries 10 "视频链接"
```

### 7.4 断点续传
```bash
# 继续上次中断的下载
yt-dlp -c "视频链接"
```

### 7.5 跳过已下载
```bash
# 使用下载归档文件，避免重复下载
yt-dlp --download-archive downloaded.txt "视频链接"
```

### 7.6 代理
```bash
# HTTP 代理
yt-dlp --proxy http://127.0.0.1:7890 "视频链接"

# SOCKS5 代理
yt-dlp --proxy socks5://127.0.0.1:1080 "视频链接"
```

---

## 八、Cookie 与登录

### 8.1 从浏览器自动读取 Cookie
```bash
# Chrome
yt-dlp --cookies-from-browser chrome "视频链接"

# Safari
yt-dlp --cookies-from-browser safari "视频链接"

# Edge
yt-dlp --cookies-from-browser edge "视频链接"

# Firefox
yt-dlp --cookies-from-browser firefox "视频链接"
```

### 8.2 使用 Cookie 文件
```bash
yt-dlp --cookies cookies.txt "视频链接"
```

### 8.3 用户名密码登录
```bash
yt-dlp -u 用户名 -p 密码 "视频链接"
```

---

## 九、后处理

### 9.1 嵌入元数据
```bash
# 嵌入缩略图
yt-dlp --embed-thumbnail "视频链接"

# 嵌入元数据（标题、描述、日期等）
yt-dlp --embed-metadata "视频链接"

# 嵌入章节信息
yt-dlp --embed-chapters "视频链接"

# 全部嵌入
yt-dlp --embed-thumbnail --embed-metadata --embed-chapters --embed-subs "视频链接"
```

### 9.2 视频转换
```bash
# 转为 mp4 格式
yt-dlp --remux-video mp4 "视频链接"

# 重新编码为 mp4
yt-dlp --recode-video mp4 "视频链接"
```

### 9.3 SponsorBlock（跳过广告片段）
```bash
# 移除赞助片段
yt-dlp --sponsorblock-remove sponsor "视频链接"

# 移除所有非内容片段
yt-dlp --sponsorblock-remove all "视频链接"

# 标记赞助片段为章节（不移除）
yt-dlp --sponsorblock-mark sponsor "视频链接"
```

### 9.4 下载特定时间段
```bash
# 下载第 30 秒到第 2 分钟的片段
yt-dlp --download-sections "*00:00:30-00:02:00" "视频链接"

# 下载前 60 秒
yt-dlp --download-sections "*00:00:00-00:01:00" "视频链接"
```

---

## 十、B 站（Bilibili）专用技巧

### 10.1 基础下载
```bash
yt-dlp "https://www.bilibili.com/video/BVxxxxxxxx"
```

### 10.2 带 Cookie 下载（解决 403 错误）
```bash
yt-dlp --cookies-from-browser chrome "https://www.bilibili.com/video/BVxxxxxxxx"
```

### 10.3 下载最高画质
```bash
yt-dlp --cookies-from-browser chrome -f "bestvideo+bestaudio/best" "B站链接"
```

### 10.4 下载合集/分P
```bash
# 下载所有分P
yt-dlp --cookies-from-browser chrome "B站链接"

# 只下载第 1-5 P
yt-dlp --cookies-from-browser chrome --playlist-items 1-5 "B站链接"
```

---

## 十一、配置文件

可以把常用参数写入配置文件，避免每次都输入：

### 配置文件位置
- **macOS/Linux**: `~/.config/yt-dlp/config`
- **Windows**: `%APPDATA%\yt-dlp\config`

### 示例配置
```ini
# 默认保存路径
-o ~/Downloads/yt-dlp/%(channel)s/%(title)s.%(ext)s

# 默认最佳画质
-f bestvideo[height<=1080]+bestaudio/best[height<=1080]

# 嵌入元数据和缩略图
--embed-metadata
--embed-thumbnail

# 使用下载归档避免重复
--download-archive ~/Downloads/yt-dlp/archive.txt

# 使用 Chrome Cookie
--cookies-from-browser chrome

# 限速 5MB/s
-r 5M
```

---

## 十二、实用组合命令

```bash
# 🎬 完美下载：1080p + 嵌入字幕/缩略图/元数据
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best" \
  --embed-subs --write-auto-subs --sub-langs "zh-Hans,en" \
  --embed-thumbnail --embed-metadata --embed-chapters \
  -o "~/Downloads/%(title)s.%(ext)s" "视频链接"

# 🎵 批量下载音乐播放列表为 MP3
yt-dlp -x --audio-format mp3 --audio-quality 0 \
  --embed-thumbnail --embed-metadata \
  -o "~/Music/%(playlist_index)02d-%(title)s.%(ext)s" "播放列表链接"

# 📺 下载整个频道的最新 10 个视频
yt-dlp --playlist-end 10 \
  -o "~/Downloads/%(channel)s/%(upload_date)s-%(title)s.%(ext)s" \
  "https://www.youtube.com/@频道名/videos"

# 📝 只获取视频信息（不下载）
yt-dlp --dump-json "视频链接" | python3 -m json.tool
```
