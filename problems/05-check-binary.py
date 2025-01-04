# Given a string, `str`, write a function, `check_binary`, that returns whether
# or not `str` is a valid binary string. While there are many ways to solve
# this, try to implement a solution using a set.

# Write your code here.
def check_binary(str):
    set1=set(str)
    # check if only 0 and 1 exist in set1
    check = [x for x in set1 if x!='0' and x!='1']
    return len(check)==0

str1 = '1010001010010100101'
str2 = '1010010015010101010'

print(check_binary(str1))       # True
print(check_binary(str2))       # False