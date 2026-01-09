def is_three_digit_and_digit_sum_divisible_by_k(n: int, k: int) -> bool:
    """
    Returns True if `n` is a three-digit integer and the sum of its digits
    is divisible by `k`.

    Args:
        n (int): The number to examine.
        k   (int): The divisor for the digitsum.

    Returns:
        bool: True when both conditions hold, otherwise False.
    """
    
    
    if not (100 <= n <= 999):
        return False

    n_str = str(n)
    digit_sum = int(n_str[0]) + int(n_str[1]) + int(n_str[2])

    return digit_sum % k == 0
    
# #Another Method:
# def is_three_digit_and_digit_sum_divisible_by_k(n: int, k: int) -> bool:
    
#     if 100<=n<=999 and ((n//100)+(n%10)+((n-(n//100)*100)//10))%k==0:
#         return True
#     else:
#         return False

# Three-Digit Number with Digit-Sum Divisible by k
# Write a function is_three_digit_and_digit_sum_divisible_by_k that takes an positive integer num and a positive integer k and returns True if both conditions are satisfied:

# num is a three digit positive number (i.e., 100 to 999).
# The sum of the decimal digits of num is divisible by k.
# If either condition fails, return False.

# Examples

# is_three_digit_and_digit_sum_divisible_by_k(145, 5)   -> True   # 1+4+5 = 10, 10 % 5 == 0
# is_three_digit_and_digit_sum_divisible_by_k(123, 5)   -> False  # 1+2+3 = 6, 6 % 5 != 0
# is_three_digit_and_digit_sum_divisible_by_k(450, 10)  -> False  # 4+5+0 = 9, 9 % 10 != 0
# is_three_digit_and_digit_sum_divisible_by_k(999, 9)   -> True   # 9+9+9 = 27, 27 % 9 == 0
# is_three_digit_and_digit_sum_divisible_by_k(1040, 5)  -> False  # not a threedigit number
# Note: This is a function-type problem. Do not read from standard input or print anything. Just implement the function.
