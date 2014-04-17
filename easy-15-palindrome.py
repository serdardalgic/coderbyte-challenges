# Have the function Palindrome(str) take the str parameter being passed and
# return the string true if the parameter is a palindrome, (the string is the
# same forward as it is backward) otherwise return the string false. For
# example: "racecar" is also "racecar" backwards. Punctuation and numbers
# will not be part of the string.


def Palindrome(str_):
    cmp_str = str_.replace(" ", "")
    return cmp_str == cmp_str[::-1] and "true" or "false"


def Palindrome2(str_):
    cmp_str = ''.join(str_.split())
    return 'true' if cmp_str == ''.join(reversed(cmp_str)) else 'false'


# keep this function call here
# to see how to enter arguments in Python scroll down
print Palindrome(raw_input())
