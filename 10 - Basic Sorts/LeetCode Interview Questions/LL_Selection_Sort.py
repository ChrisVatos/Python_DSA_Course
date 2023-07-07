class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
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
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE SELECTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def selection_sort(self):

        if self.length <= 1:
            return self.head
         
        starter_node = self.head
        for i in range(self.length - 1, 0, -1):
            min_value = starter_node.value
            running_tmp = starter_node.next
            while running_tmp:
                if running_tmp.value < min_value:
                    min_value = running_tmp.value
                    node_to_swap = running_tmp
                running_tmp = running_tmp.next
            if min_value != starter_node.value:
                tmp_value = starter_node.value
                starter_node.value = node_to_swap.value
                node_to_swap.value = tmp_value
            starter_node = starter_node.next
        return self.head








my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

