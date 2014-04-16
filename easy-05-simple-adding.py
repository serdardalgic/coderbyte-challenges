# Have the function SimpleAdding(num) add up all the numbers from 1 to num. For
# the test cases, the parameter num will be any number from 1 to 1000.


def SimpleAdding(num):
    sum = 0
    for num in xrange(1, num + 1):
        sum += num
    return sum


def SimpleAdding2(num):
    return reduce(lambda x, y: x + y, [n for n in xrange(1, num + 1)])


def SimpleAdding3(num):
    return sum(xrange(1, num + 1))


def SimpleAdding4(num):
    return (num * (num + 1)) / 2


# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleAdding(raw_input())
