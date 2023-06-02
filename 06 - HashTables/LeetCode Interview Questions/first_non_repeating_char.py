# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(string):

    letters_dict = {}

    for letter in string:
        letters_dict[letter] = letters_dict.get(letter, 0) + 1

    for letter in string:
        if letters_dict[letter] == 1:
            return letter
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""