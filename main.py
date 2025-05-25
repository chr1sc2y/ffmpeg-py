from conversion import *

if __name__ == "__main__":
    dir="/home/zintrulcre/tst"
    traverse(dir, ".png", compress_image, "original", "jpg")
    # traverse(dir, ".mp4", compress_video, "1920:1080", 60)  # drone
    # traverse(dir, ".mp4", compress_video, "3840:2160", 60) # camera
