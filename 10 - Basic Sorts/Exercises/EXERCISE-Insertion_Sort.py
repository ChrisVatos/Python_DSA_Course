## WRITE INSERTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        tmp = my_list[i]
        j = i - 1
        while tmp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = tmp
            j -= 1
    return my_list




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

