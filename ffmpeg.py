# todo: import ffmpeg
from context import FileContext
from conversion import *

if __name__ == "__main__":
    source_dir = "C:/Users/Administrator/Downloads/test"
    traverse(source_dir, ".mp4", convert_to_1080p_30fps)