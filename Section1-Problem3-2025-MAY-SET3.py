def add_average_key_diff(d: dict, k1, k2) -> None:
    """
    Add a new key-value pair to the dictionary inplace:
        new key   = round(average of k1 and k2)
        new value = absolute difference of the two values

    The function does **not** return anything; it mutates ``d`` directly.

    Args:
        d (dict): Dictionary containing ``k1`` and ``k2``.
        k1, k2: Existing keys (numeric).

    Returns:
        None
    """
    
    
    new_key = round((k1 + k2) / 2)
    new_val = abs(d[k1] - d[k2])
    d[new_key] = new_val
    

# #Another Method:

# def add_average_key_diff(d: dict, k1, k2) -> None:
 
#     d[round((k1+k2)/2)]=abs(d[k1]-d[k2])

# Add average key with absolute difference value (in-place)
# Write a function add_average_key_diff(d, k1, k2) that receives a dictionary d and two existing keys k1 and k2.

# The function should:

# Compute the average of the two keys and round it to the nearest integer (use Pythons builtin round).
# Compute the absolute difference between the values stored for k1 and k2.
# Insert a new entry average_key : absolute_difference into d.
# Do not return anything the dictionary is modified inplace.
# Assume k1 and k2 are present in d and their values are numeric (int or float). The new key is stored as an int.

# NOTE: This is a function-type question you only need to implement the function, no input/output handling is required.

# Example

# >>> d = {2: 10, 8: 30}
# >>> add_average_key_diff(d, 2, 8)
# >>> d
# {2: 10, 8: 30, 5: 20}

