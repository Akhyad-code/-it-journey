import os

files = os.listdir(".")

print("Files in current folder:")
for item in files:
    print(item)