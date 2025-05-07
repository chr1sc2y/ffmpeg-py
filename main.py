from conversion import *

if __name__ == "__main__":
    dir = "/Users/zintrulcre/Downloads/temp"
    # traverse(dir, ".png", compress_image, "3840:2160", "jpg")
    traverse(dir, ".mp4", compress_video, "1920:1080", 60)  # drone
    # traverse(dir, ".mp4", compress_video, "3840:2160", 60) # camera
