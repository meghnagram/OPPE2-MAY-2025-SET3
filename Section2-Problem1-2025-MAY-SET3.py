def count_special(words):
    """
    Counts how many words in the given list have the same first and last
    characters (case-insensitive) but different second and secondlast
    characters (also case-insensitive).

    Args:
        words (list of str): List of words to examine.

    Returns:
        int: Number of words satisfying the conditions.

    Examples:
        >>> count_special(["Bulb", "deed", "civic", "Noon"])
        1
        >>> count_special(["abca", "aXba", "xyzzyx", "abcaXab"])
        2
    """
    
    
    count = 0
    for w in words:
        w_low = w.lower()
        # word length is guaranteed >= 2, so indexing is safe
        if w_low[0] == w_low[-1] and w_low[1] != w_low[-2]:
            count += 1
    return count
    

# #Another Method:
# def count_special(words):
#     """
#     Counts how many words in the given list have the same first and last
#     characters (case-insensitive) but different second and secondlast
#     characters (also case-insensitive).

#     Args:
#         words (list of str): List of words to examine.

#     Returns:
#         int: Number of words satisfying the conditions.

#     Examples:
#         >>> count_special(["Bulb", "deed", "civic", "Noon"])
#         1
#         >>> count_special(["abca", "aXba", "xyzzyx", "abcaXab"])
#         2
#     """
#     result=0
#     for i in words:
#         if i[0].lower()==i[-1].lower() and i[1].lower()!=i[-2].lower():
#             result +=1 
#     return result

# Count Words with Matching First/Last but Different Second/Second-Last Letters
# Write a function count_special(words) that receives a list of words (strings) and returns the number of words that satisfy both of the following conditions (the check is case-insensitive):

# The first and the last characters of the word are the same.
# The second character and the secondlast character of the word are different.
# Assume each word has at least two characters.

# NOTE: This is a functiontype question. You do not need to read input or print output; just implement the function and return the required integer.

# Example
# is_equal(count_special(["Bulb", "deed", "civic", "Noon", "lol"]), 1)
# # "Bulb": B == b (yes), u != l (yes) -> counted
# # "deed": d == d (yes), e != e (no) -> not counted
# # "civic": c == c (yes), i != i (no) -> not counted
# # "Noon": N == n (yes), o != o (no) -> not counted
# # result = 1
# is_equal(count_special(["abca", "aXba", "xyzzyx", "abcaXab"]), 2)
# # "abca":   a == a (yes), b != c (yes) -> counted
# # "aXba":   a == a (yes), X != b (yes) -> counted
# # "xyzzyx": x == x (yes), y != y (no)  -> not counted
# # "abcaXab": a == b (no)               -> ignored
# # result = 2

  
