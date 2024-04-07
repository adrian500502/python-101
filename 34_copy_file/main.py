# copyfile() = copies contents of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)

import shutil

# shutil.copyfile("test.txt", "copy.txt") #src, dst
# shutil.copyfile("test.txt", "C:\\Users\\someone\\Desktop\\copy.txt") #src, dst
shutil.copy2("test.txt", "C:\\Users\\someone\\Desktop\\copy.txt") #src, dst