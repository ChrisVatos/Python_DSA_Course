# WRITE ROTATE FUNCTION HERE #
#                            #
#                            #
#                            #
#                            #
##############################
def rotate(nums, k):
    nums_from_start = len(nums) - k

    for i in range(len(nums), nums_from_start, -1):
        nums.insert(0, nums.pop())
    


    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""