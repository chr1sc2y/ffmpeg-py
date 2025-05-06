from conversion import traverse, compress_image

dir = input("Please input the dir, e.g. /home/zintrulcre/data/: ")
print(dir)
traverse(dir, ".png", compress_image, "3840:2160", "jpg")