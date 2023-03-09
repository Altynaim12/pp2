import os

example = "C:\\Users\\Алтынай\\Desktop\\w3\\files"

print("Directories: ")
for i in os.listdir(example):
    if os.path.isdir(os.path.join(example, i)):
        print(i)
print("Files: ")
for i in os.listdir(example):
    if os.path.isfile(os.path.join(example, i)):
        print(i)

print("Directories and files together: ")
for i in os.listdir(example):
    print(i)