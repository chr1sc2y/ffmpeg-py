# ffmpeg-py

Video and image processing toolkit based on FFmpeg.

## Quick Start

### Drone Video Compression

```bash
cd scripts
python3 drone_video.py
```

Compress drone videos to 1080p @ 15Mbps while keeping original frame rate.
- Optimized for DJI drone footage
- High quality for mobile viewing
- Original videos archived to `archive/` subdirectory
- ~112MB per minute

### Image Format Conversion

```bash
cd scripts
python3 convert_png_to_jpg.py
```

Converts PNG to JPG format.

## Project Structure

- `src/` - Core implementation modules
- `scripts/` - Preset scripts
