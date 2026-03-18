import os

folder = "."
items = os.listdir(folder)

txt_count = 0
py_count = 0
png_count = 0

for item in items:
    if item.endswith(".txt"):
        txt_count += 1
    elif item.endswith(".py"):
        py_count += 1
    elif item.endswith(".png"):
        png_count += 1

print("TXT:", txt_count)
print("PY:", py_count)
print("PNG:", png_count)