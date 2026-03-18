files = ["notes.txt", "report.pdf", "script.py", "image.png"]

for file in files:
    if file.endswith(".txt"):
        print(file, "- text file")
    else:
        print(file, "- not a text file")