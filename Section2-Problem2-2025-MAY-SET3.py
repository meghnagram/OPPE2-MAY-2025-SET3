def group_by_remainder(nums, k):
    """Return a dict mapping each occurring remainder to a sorted list of numbers."""
    rem_dict = {}
    for num in nums:
        r = num % k
        rem_dict.setdefault(r, []).append(num)
    return rem_dict


nums = [int(x) for x in input().split(',')]
k = int(input())

result = group_by_remainder(nums, k)

for key in sorted(result.keys()):
    values = ','.join(str(v) for v in result[key])
    print(f"{key} - {values}")

# #Another Method:

# # Write your code here

# newstr=input()
# l=newstr.split(',')

# div=int(input())

# d={}

# for i in range(div):
#     d[i]=[]
    
    
# for i in l:
#     c=int(i.strip())%div
#     d[c].append(i)

# for k,v in d.items():
#     if len(v) >0:
#         print (f"{k} - {','.join(v)}")


# Remainder Grouping Dictionary
# Write a Python program that reads two inputs from the user:

# A single line containing a list of integers separated by commas. The line may contain arbitrary spaces around the commas.
# An integer k - the divisor.
# Your task is to build a dictionary that groups the numbers by their remainder when divided by k.

# Each key is a remainder r (0<=r<k) that actually appears among the given numbers.
# The value for a key r is a list of all numbers whose remainder equals r, sorted in ascending order.
# Print the dictionary in ascending order of the keys using the following format (one key per line) with values in ascending order.:

# key1 - val1,val2,...
# key2 - val1,val2,...
# ...
# There must be no extra spaces around the dash or the commas.
    
