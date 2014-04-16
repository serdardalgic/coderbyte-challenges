# Have the function TimeConvert(num) take the num parameter being passed and
# return the number of hours and minutes the parameter converts to (ie.
# if num = 63 then the output should be 1:3). Separate the number of hours
# and minutes with a colon.


def TimeConvert(num):
    return "{hour}:{minute}".format(hour=num / 60, minute=num % 60)


def TimeConvert2(num):
    return str(num / 60) + ":" + str(num % 60)


# keep this function call here
# to see how to enter arguments in Python scroll down
print TimeConvert(raw_input())
