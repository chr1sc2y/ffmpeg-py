# todo: import ffmpeg
from context import FileContext
from conversion import *

if __name__ == "__main__":
    source_dir = "~/Download/test"
    traverse(source_dir, ".mp4", compress_crf_28)
    # traverse(source_dir, ".mov", convert_to_1080p_30fps)
    # traverse(source_dir, ".png", convert_images_to_1080p)
    # traverse(source_dir, ".jpg", convert_images_to_1080p)
    # traverse(source_dir, ".jpeg", convert_images_to_1080p)
