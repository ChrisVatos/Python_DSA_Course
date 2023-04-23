class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # WRITE PARTITION_LIST METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def partition_list(self, x):
        if self.head is None:
            return None
        
        dummy_Node_Less_Than_X = Node(0)
        dummy_Node_Greater_Than_X = Node(0)
        prev1 =   dummy_Node_Less_Than_X
        prev2 =  dummy_Node_Greater_Than_X

        current = self.head

        while current is not None:
            if (current.value < x):
                prev1.next = current
                prev1 = current
            else: 
                prev2.next = current
                prev2 = current
            current = current.next

        prev2.next = None
        prev1.next =  dummy_Node_Greater_Than_X.next
        self.head =  dummy_Node_Less_Than_X.next
        self.tail = prev2



ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
