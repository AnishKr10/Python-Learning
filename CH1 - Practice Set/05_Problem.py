# Label the program written in problem 4 with comments

import os

# Specify the directory path
path = "/"

# Get and print all files and folders in the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)