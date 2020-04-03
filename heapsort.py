def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    # See if left child is greater than root (if exists)
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    # See if right child is greater than root (if exists)    
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    # change the root node with the largest values
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size) # recursive function call
    return unsorted

unsorted = [4,14,7,2,8,1]

# The main function to sort an array of given size
def heapsort(arr):
    heap_size = len(arr)
 
    # Build a maxheap.
    for idx in range(heap_size, -1, -1):
        heapify(arr, idx, heap_size)
    
    # Swap & Max-heap
    for idx in range(heap_size-1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]   # swap
        heapify(arr, 0, idx)
 
arr = [ 5, 4, 6, 1, 2, 3]
heapsort(arr)
heap_size = len(arr)
for i in range(heap_size):
    print ("%d" %arr[i]),