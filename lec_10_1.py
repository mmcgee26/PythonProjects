# sequential search

def ssearch(alist, n):
    for i in alist:
        if i == n:
            return True
    return False

print(ssearch([4,3,1,2], 1))

# binary search

def bsearch(alist,x):
    f = 0
    l = len(alist) - 1
    found = False
    while (l > f) and (found == False):
        m = (f + l) // 2
        if alist[m] == x:
            found = True
        else:
            if alist[m] > x:
                l = m - 1
            else:
                f = m + 1
    return found

print(bsearch([2,4,6,7,8,9],8))

