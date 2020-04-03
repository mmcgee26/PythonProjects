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
print(heapify(unsorted, 1, 6))