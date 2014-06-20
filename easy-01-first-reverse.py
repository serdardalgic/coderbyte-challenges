# Question: Have the function FirstReverse(str_) take the str parameter
# being passed and return the string in reversed order.


def FirstReverse(str_):
  # code goes here
    rev = ""
    for x in reversed(str_):
        rev += x
    return rev


def FirstReverse2(str_):
    return str_[::-1]


def FirstReverse3(str_):
    return "".join([x for x in reversed(str_)])


# keep this function call here
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())
