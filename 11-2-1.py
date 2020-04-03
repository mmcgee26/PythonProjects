# merge sort
print('merge sort')
def merge_sort(a):
    if len(a) <= 1: return a
    
    # split (divide)
    half = len(a) // 2    
    L = merge_sort(a[:half])   # left half
    R = merge_sort(a[half:])   # right half
    merge = []                 # merge data into this list
     
    # merge (concour) 
    while len(L) > 0 and len(R) > 0:
        if L[0] > R[0]:  # left > right
            merge.append(R[0])
            R.pop(0)     # pop the 1st item from the right
        else:            
            merge.append(L[0])
            L.pop(0)     # pop the 1st item from left
    # append the remining elements to the result if L or R is empty
    if len(L) > 0: merge += L
    if len(R) > 0: merge += R
    # return the result
    return merge


a = [5,2,4,7,1,3,2,6]
print('original data set ', a)
print(merge_sort(a))

# quick sort
print('\n\nquick sort')
def quicksort(alist,l,r):
	if l > r : return
	p = r # pivot
	s = l # swap_position
	for i in range(l,r):
		if alist[i] < alist[p]:
			alist[s], alist[i] = alist[i], alist[s]
			s = s + 1 
	alist[s],alist[p] = alist[p],alist[s]
	
	quicksort(alist,l,s-1)
	quicksort(alist,s+1,r)

alist = [5,8,4,7,1,2,0,3]
print('original data set ', alist)
quicksort(alist,0,len(alist)-1)
print(alist)