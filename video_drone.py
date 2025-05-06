from conversion import compress_video, traverse

dir = input("Please input the dir, e.g. /home/zintrulcre/data/: ")
print(dir)
traverse(dir, ".mp4", compress_video, "1920:1080", 60)