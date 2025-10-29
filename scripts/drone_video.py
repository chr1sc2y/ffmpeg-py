import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import compress_drone_video, traverse

dir = input("📁 Enter directory path: ").strip().strip("'").strip('"')

# Compress drone videos to 1080p @ 15Mbps (keeps original fps)
# Compressed files are saved to 'compressed/' subdirectory
# Original files remain untouched in their original location
traverse(dir, ".mp4", compress_drone_video, "1920:1080", "15M", None)