from conversion import *

if __name__ == "__main__":
    dir="/home/zintrulcre/e/videos"
    # traverse(dir, ".png", compress_image, "3840:2160", "jpg")
    traverse(dir, ".mp4", compress_video, "1920:1080", 60)
