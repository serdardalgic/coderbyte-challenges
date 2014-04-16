# Have the function FirstFactorial(num) take the num parameter being passed and
# return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the
# test cases, the range will be between 1 and 18.


def FirstFactorial(num):
    """ Iterative version """
    r = 1
    for x in xrange(2, num + 1):
        r *= x
    return r


def FirstFactorial2(num, f=1):
    """
    Tail recursive version of factorial
    """
    return (num == 1) and f or FirstFactorial2(num - 1, num * f)


# keep this function call here
# to see how to enter arguments in Python scroll down
print FirstFactorial(int(raw_input()))
