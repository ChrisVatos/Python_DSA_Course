
# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def find_pairs(list1, list2, target):
    set2 = set(list2)
    pairs = []
    for num in list1:
        complement = target - num
        if complement in set2:
            pairs.append((num, complement))
    return pairs



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""