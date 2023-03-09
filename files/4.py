

example = "C:\\Users\\Алтынай\\Desktop\\w3\\files\\text.txt"


with open(example, 'r') as e:
    lines = e.readlines()

num_lines = len(lines)
# for i in lines:
#     print(i)
print(f'The file has {num_lines} lines.')