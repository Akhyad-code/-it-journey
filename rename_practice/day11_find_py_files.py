import os

folder = "."
items = os.listdir(folder)

for item in items:
    if item.endswith(".py"):
        print("Python file found:", item)