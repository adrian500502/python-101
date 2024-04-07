import os

# source = "test.txt"
source = "folder"
# destination = "C:\\Users\\someone\\Desktop\\test.txt"
destination = "C:\\Users\\someone\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

