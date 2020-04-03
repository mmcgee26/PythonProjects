# bubble sort
def bubble(lst):
    n = len(lst) - 1                # number of items - 1
    for i in range(n):
        for j in range(n-i):        # from the 1st (index 0) to the n-i th items
            if lst[j] > lst[j+1]:   # if they're not in ascending order
                lst[j], lst[j+1] = lst[j+1], lst[j]  # swap
    return lst
lst = [2,4,5,3,1]
print(bubble(lst))

# selection sort
def selection(lst):
    num = len(lst)    # number of items
    for i in range(num):
        largest = 0
        for j in range(num - i):        # from the 1st (index 0) to n-1 th items
            if lst[j] > lst[largest]:   # if the current item is > the largest item
                largest = j             # update the index of the largest item
        lst[largest], lst[j] = lst[j], lst[largest] #swap
    return lst
lst = [2,4,5,3,1]
print(selection(lst))

# insertion sort
def insertion(lst):
    for i in range(1,len(lst)): # read 4,5,3,1
        temp = lst[i]           # take the 1st item from the unsorted list
        pt = i                  # index of the last item of the unsorted list
        while pt > 0 and lst[pt - 1] > temp: # shift items that are > temp
            lst[pt] = lst[pt-1]
            pt = pt - 1
        lst[pt] = temp          # insert the temp to the correct place
    return lst
lst = [2,4,5,3,1]
print(insertion(lst))
