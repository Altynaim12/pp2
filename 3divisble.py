n = int(input())
divBy7 = [i for i in range (1,n) if (i % 3 == 0 and i % 4 == 0)]


def divChecker(n):
    for i in range(1,n):
        if i % 3 == 0 and i % 4 == 0:
            print(i)
        

divChecker(n)
