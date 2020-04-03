# adding 1-4, iterative method
def iterative(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum
print(iterative(4))

# adding 1-4, recursive method
def recursive(n):
    if n == 0:
        return 0
    return n + recursive(n-1)
print(recursive(4))

# num to bin, iterative method
def toBinI(n):
    bstr = ''
    while (n != 0):
        n = n // 2
        r = n % 2
    
        bstr = bstr + str(r)
    print(bstr)

toBinI(14)


