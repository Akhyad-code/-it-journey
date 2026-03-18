import os

folder = "."
items = os.listdir(folder)

for item in items:
    if item.endswith(".txt"):
        print(item)