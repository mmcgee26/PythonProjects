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
        print (node.val)
        if node.next == None:
            break
        node = node.next

# remove a node from the linked list
def remove(rnode):
    current = head.next
    previous = head
    while True:
        if current == rnode:
            previous.next = current.next
            break
        elif current.next == None:
            previous.next = current.next
            break
        previous = current
        current = current.next

print_linked_list(head)
print('')    
remove(n1) # test it with n2 and n3
print_linked_list(head)    
