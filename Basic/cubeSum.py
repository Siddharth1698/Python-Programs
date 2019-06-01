
def cubesum(n):
    sm = 0
    for i in range(0,n+1):
        sm = sm + i*i*i
    return sm


print("The square sum of is ", cubesum(2))