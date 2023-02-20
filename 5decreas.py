def rev():
    for i in range(n, -1, -1):        
        yield i
n = int(input())
for x in rev():
    print(x)