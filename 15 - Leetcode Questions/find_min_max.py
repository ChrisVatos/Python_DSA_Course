# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def find_max_min(inputList):
    max = inputList[0]
    min = inputList[0]

    for number in inputList:
        if number < min:
            min = number
        if number > max:
            max = number

    return max, min
    



print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""