# Question: Have the function FirstReverse(str) take the str parameter
# being passed and return the string in reversed order.


def FirstReverse(str):
  # code goes here
    rev = ""
    for x in reversed(str):
        rev += x
    return rev


def FirstReverse2(astr):
    return astr[::-1]


def FirstReverse3(astr):
    return "".join([x for x in reversed(astr)])


# keep this function call here
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())
