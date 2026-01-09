def remove_second_and_second_last(s: str) -> str:
    """
    Return a new string after removing the second character (index 1)
    and the second-last character (index len(s)-2). If the length of
    the string is less than 4, return the original string.

    Args:
        s (str): Input string.

    Returns:
        str: Modified string.

    Examples:
        >>> remove_second_and_second_last("abcdef")
        'acdf'
        >>> remove_second_and_second_last("abcd")
        'ad'
    """
    
    
    if len(s) < 4:
        return s
    # remove character at index 1 and at index len(s)-2
    return s[:1] + s[2:-2] + s[-1]
    
# #Another Method:

# def remove_second_and_second_last(s: str) -> str:
   
#     if len(s)<4:
#         return s 
#     else:
#         return s[0]+s[2:-2]+s[-1]
    
# Remove Second and Second-Last Character from String
# Write a function remove_second_and_second_last(s) that receives a string s and returns a new string obtained after removing the second character (index1) and the second-last character (index len(s)-2).

# Assume the string will have atleast 4 characters

# NOTE: This is a functiontype question; you do not need to read input or print output, just implement the function.

# Examples

# remove_second_and_second_last("abcdef") -> "acdf"
# (remove 'b' at index1 and 'e' at index4)
# remove_second_and_second_last("abcd") -> "ad"
# (remove 'b' at index1 and 'c' at index2)


