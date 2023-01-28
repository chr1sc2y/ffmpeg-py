import os
path = './temp/'
file_list = []

lst = os.listdir(path)
lst.sort()
a = 3049
b = 3050

for file in lst:
    name = file
    # print("_DSF" + str(a) + ".JPG")
    # print(name)
    if name == "_DSF" + str(a) + ".JPG":
        a += 3
        os.remove("./temp/" + name)
        # print(name)
    if name == "_DSF" + str(b) + ".JPG":
        b += 3
        os.remove("./temp/" + name)
        # print(name)
    file_list.append(file)

