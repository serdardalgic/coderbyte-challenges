# Have the function ABCheck(str) take the str parameter being passed and return
# the string true if the characters a and b are separated by exactly 3 places
# anywhere in the string at least once (ie. "lane borrowed" would result in
# true because there is exactly three characters between a and b). Otherwise
# return the string false.


def ABCheck(str_):
    for i in range(0, len(str_) - 4):
        if (str_[i], str_[i + 4]) in [('a', 'b'), ('b', 'a')]:
            return "true"
    return "false"


# keep this function call here
# to see how to enter arguments in Python scroll down
print ABCheck(raw_input())
