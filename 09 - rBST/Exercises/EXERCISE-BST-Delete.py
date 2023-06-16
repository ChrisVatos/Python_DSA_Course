class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
 

    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

 
          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    ## WRITE DELETE_NODE METHODS HERE ##
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def __r_delete(self, currentNode, value):
        if currentNode == None:
            return None
        if value < currentNode.value:
            currentNode.left = self.__r_delete(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self.__r_delete(currentNode.right, value)
        else:
            if currentNode.left == None and currentNode.right == None:
                return None
            elif currentNode.left == None:
                currentNode = currentNode.right
            elif currentNode.right == None:
                currentNode = currentNode.left
            else:
                min_value = self.min_value(currentNode.right)
                currentNode.value = min_value
                currentNode.right = self.__r_delete(currentNode.right, min_value)
        return currentNode

    def r_delete(self, value):
        return self.__r_delete(self.root, value)
    
    def min_value(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value



my_tree = BinarySearchTree()
my_tree.r_insert(9)
my_tree.r_insert(7)
my_tree.r_insert(8)


"""
       2
      / \
     1   3
"""

# print("root:", my_tree.root.value)
# print("root.left =", my_tree.root.left.value)
# print("root.right =", my_tree.root.right.value)


my_tree.r_delete(7)

# """
#        3
#       / \
#      1   None
# """


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""

