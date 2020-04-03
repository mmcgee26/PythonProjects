def aster(n):
    if(n==0):
        return ''
    return '*' + aster(n-1)
print(aster(5))
    