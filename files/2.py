import os

example = "C:\\Users\\Алтынай\\Desktop\\w3\\files\\text.txt"


if os.path.exists(example):
    print('Path exists!!!')
    if os.access(example, os.R_OK):
        print('It is readable.')
    else:
        print('It is not readable.')
    if os.access(example, os.W_OK):
        print('It is writable.')
    else:
        print('It is not writable.')
    if os.access(example, os.X_OK):
        print('It is executable.')
    else:
        print('It is not executable.')
else:
    print('Path does not exist!!!')