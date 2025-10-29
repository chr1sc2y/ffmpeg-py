"""
FFmpeg Python wrapper for video and image compression.
"""

# Core utilities
from .core import traverse, FileContext

# Video processing
from .video_processing import (
    compress_video,
    compress_drone_video,
    compress_rate,
    convert_webm_to_mp4,
    get_video_bitrate,
    get_video_fps,
    get_video_resolution,
    format_file_size,
    print_video_info,
)

# Image processing
from .image_processing import compress_image

__all__ = [
    # Core
    "traverse",
    "FileContext",
    # Video
    "compress_video",
    "compress_drone_video",
    "compress_rate",
    "convert_webm_to_mp4",
    "get_video_bitrate",
    "get_video_fps",
    "get_video_resolution",
    "format_file_size",
    "print_video_info",
    # Image
    "compress_image",
]
