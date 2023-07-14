# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
def find_longest_string(strings):

    longest = strings[0]

    for string in strings:

        if len(string) > len(longest):
            longest = string

    return longest

    


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""