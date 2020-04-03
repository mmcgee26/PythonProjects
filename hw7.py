def bsearch(arr, val, first=0, last=None):
    if last is None:
        last = len(arr) - 1
    if first > last:
        return False

    mid = (first + last) // 2
    if val == arr[mid]:
        return mid
    if val < arr[mid]:
        return bsearch(arr, val, first, mid-1)
    # elem > arr[mid]
    return bsearch(arr, val, mid+1, last)
a = [1,2,3,4,5,6,7,8,10]
print (bsearch(a, 5, 0, len(a)-1)) #false
print (bsearch(a, 2, 0, len(a)-1))
