# todo: import ffmpeg
from context import FileContext
from conversion import *

if __name__ == "__main__":
    source_dir = "~/Downloads"
    traverse(source_dir, ".mp4", compress_video, "1280:720", 30, 28)
    traverse(source_dir, ".jpg", compress_image, "1280:720")
