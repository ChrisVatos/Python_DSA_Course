# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum(list, target):

    numbers_dict = {}

    for i in range(len(list)):
        complementary = target - list[i]

        if complementary in numbers_dict:
            return [numbers_dict[complementary], i]
        
        numbers_dict[list[i]] = i
   
    return []
    
    
    
    
print ( two_sum([2, 7, 11, 15], 9) )
print ( two_sum([3, 2, 4], 6) )
print ( two_sum([3, 3], 6) )
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [0, 1]
    [1, 2]
    [0, 1]
    []
    [2, 3]
    [0, 1]
    []

"""


