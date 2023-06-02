class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ## WRITE INSERT METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node

        tmp = self.root
        while (True):

            if new_node.value == tmp.value:
                return False
            
            if value < tmp.value and tmp.left is None:
                tmp.left = new_node
                return True
            
            if value > tmp.value and tmp.right is None:
                tmp.right = new_node
                return True

            if value < tmp.left.value:
                tmp = tmp.left

            if value > tmp.right.value:
                tmp = tmp.right

           





my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""