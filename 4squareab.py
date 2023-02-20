# 4
def absqrt():
    for i in range(a, b + 1):        
        yield i ** 2

a = int(input())
b = int(input())
for x in absqrt():    
    print(x)

