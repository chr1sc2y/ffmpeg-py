# todo: import ffmpeg
from conversion import *

if __name__ == "__main__":
    dir = "/Users/zintrulcre/Downloads/temp"
    traverse(dir, ".png", compress_image, "3840:2160", "jpg")
    # traverse(source_dir, ".mp4", compress_video, "1280:720", 30, 28)
    # traverse(source_dir, ".mp4", compress_video, "1280:720", 30, 28)
