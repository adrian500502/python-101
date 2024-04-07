import os
import shutil

path = "test.txt"
# path = "empty_folder"
# path = "folder"

try:
    os.remove(path)   # delete a file
    # os.rmdir(path)    # delete an empty directory
    # shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to delete that!")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " has been deleted")