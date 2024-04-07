import os

path = "C:\\Users\\someone\\Desktop\\Repos\\python-101\\31_file_detection\\file.txt" # has to be adjusted individually

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")