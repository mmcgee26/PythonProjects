# Homework 9
# The BST usually doesn't allow duplicated items. hw9.py produces a wrong BST. 
# Modify our implementation of the binary search tree so that it handles duplicate keys properly. 
# That is, if a key is already in the tree then the new payload should replace the old rather than add another node with the same key.


# correct BST
#    10
#   /  \
#  6    14
# / \   /\
#4   8 12 16


# with current implementation, the BST is
#    10
#   /  \
#  6    14
# / \   /\
#4   8 12 16
# \
#  6   
# modify the insert function to create a correct BST

class Node:
    def __init__(self, val):
        self.left = None # pointer to the left subtree
        self.right = None # pointer to the right subtree
        self.data = val     # key (node value)

class BST:
    
    def __init__(self,data):        # Binary Search Tree init
        self.root = Node(data)
#############
############# DO NOT MODIFY ABOVE THIS LINE : 0 POINT IF YOU DO SO ##########
    global checklist
    checklist = []
    def insert(self,data,node=None):
        if node is None:            # need it to start the recursive function
            node = self.root
        checker = True
        
        if data in checklist:
            checker = False
        
        
        if checker:
            if data > node.data:# if the value to be inserted is > node value
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.insert(data,node.right)
            else:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.insert(data,node.left)
        else:
            return
        if checker:
            checklist.append(data)

############# DO NOT MODIFY BELOW THIS LINE : 0 POINT IF YOU DO SO ##########
#############
    def levelorderwithLevelInfo(self,root):
	    queue = [root]
	
	    while queue != []:
		    level_node = len(queue)
		    while level_node > 0:
			    node = queue.pop(0)
			    if node.left: queue.append(node.left)
			    if node.right: queue.append(node.right)
			    print(node.data, end = " ")
			    level_node -= 1
		    print("")
             
if __name__=='__main__':
    bst = BST(5)
    bst.insert(30)
    bst.insert(2)
    bst.insert(40)
    bst.insert(25)
    bst.insert(4)
    #<-------- adding 6 again

    print('6 should not be added twice - it is a wrong BST \n ')
    bst.levelorderwithLevelInfo(bst.root)

