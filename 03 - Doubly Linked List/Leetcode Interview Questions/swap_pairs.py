class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    # WRITE SWAP_PAIRS METHOD HERE #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    def swap_pairs(self):
        # Create a dummy node to simplify swapping logic
        dummy = Node(0)
        # Connect the dummy node to the head of the list
        dummy.next = self.head
        # Set 'prev' to the dummy node for the first iteration
        prev = dummy
    
        # Iterate while there are at least two nodes left
        while self.head and self.head.next:
            # Identify the first node of the pair to swap
            first_node = self.head
            # Identify the second node of the pair to swap
            second_node = self.head.next
    
            # Update 'next' pointers to swap the node pair
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            # Update 'prev' pointers for the swapped nodes
            second_node.prev = prev
            first_node.prev = second_node
            # Set the 'prev' of the node after the pair
            if first_node.next:
                first_node.next.prev = first_node
    
            # Move 'head' to the next pair of nodes
            self.head = first_node.next
            # Update 'prev' to the last node in the pair
            prev = first_node
    
        # Set the new head of the list after swapping
        self.head = dummy.next
        # Ensure the new head's 'prev' does not point to dummy
        if self.head:
            self.head.prev = None




my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""