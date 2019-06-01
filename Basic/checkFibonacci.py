import math

def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s * s == n

def isfib(num):
    return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4)

for i in range(1,11):
    if(isfib(i) == True):
        print(i ,"is a fibbonaci num")
    else: print(i, "is not a fib num")