import os

example = "C:\\Users\\Алтынай\\Desktop\\w3\\files\\text.txt"



if os.path.exists(example):
    if os.access(example, os.W_OK):
        os.remove(example)
        print(f"{example} deleted successfully.")
    else:
        print(f"You don't have access to delete {example}.")
else:
    print(f"{example} does not exist!")