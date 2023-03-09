import os

example = "C:\\Users\\Алтынай\\Desktop\\w3\\files\\text.txt"


if os.path.exists(example):
    print('Path exists!!!')
    filename = os.path.basename(example)
    directory = os.path.dirname(example)
    print(f'Filename: {filename}')
    print(f'Directory: {directory}')
else:
    print('Path does not exist!!!')