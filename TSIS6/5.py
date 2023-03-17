import os

# print the current directory
print("The current directory:", os.getcwd())
if not os.path.isdir("folder"):
    os.mkdir("folder")
os.chdir("folder")