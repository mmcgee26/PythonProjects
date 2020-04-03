class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

# create a linked list (adding nodes) that is identified as 'head'
head = Node(None)
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
head.next = n1
n1.next = n2
n2.next = n3

# print the linked list
def print_linked_list(head):
    node = head.next
    while True:
        print (node.val, end=' ')
        if node.next == None:
            break
        node = node.next

print_linked_list(head)
print('')

##################### code for lecture 6_2 #############################

def add_to_ordered(head, new_node):
    '''
    if head.next == None:       # if the Linked_List is empty
        head.next = new_node    # add the new_node to the List and
    return                      # terminate the function
    '''
    current = head.next
    previous = head

    while True:
        
        if current.next == None: 
            new_node.next = None
            current.next = new_node
            break
        elif current.val >= new_node.val:
            new_node.next = previous.next
            previous.next = new_node
            break
        else:
            previous = current
            current = current.next

n4 = Node(15)
add_to_ordered(head,n4) # add 15
n5 = Node(40)
add_to_ordered(head,n5) # add 40
print_linked_list(head)
print('')

##########################
def search(head, data):
    node = head.next
    result = False
    while True:
        if node.val == data:
            result = True
            break
        if node.next == None:
            break
        node = node.next

    return result

r = search(head,240)
print(r)

#########################
def size(head):
    '''
    if node.next == None:
        return 0 
    '''

    node = head.next
    count = 0
    while True:
        count = count + 1
        if node.next == None:
            break
        node = node.next
    return count

r = size(head)
print('num of nodes :', r)
