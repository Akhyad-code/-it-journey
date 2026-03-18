import os

folder = "."
items = os.listdir(folder)

count = 0

for item in items:
    if item.endswith(".txt"):
        count += 1

print("TXT files:", count)