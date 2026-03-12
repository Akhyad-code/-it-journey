import os

folder_name = "python_created_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created")
else:
    print("Folder already exists")