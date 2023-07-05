## WRITE BUBBLE_SORT FUNCTION HERE ##
#                                   #
#                                   #
#                                   #
#                                   #
##################################### 
def bubble_sort(my_list):
    ## After each run of the outer loop, the largest number during that run is in the correct position at the end of the list
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
    return my_list

print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """