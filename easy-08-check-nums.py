# Have the function CheckNums(num1,num2) take both parameters being passed and
# return the string true if num2 is greater than num1, otherwise return the
# string false. If the parameter values are equal to each other then return the
# string -1.


def CheckNums(num1, num2):
    if num1 == num2:
        return "-1"
    return "true" if num2 > num1 else "false"


def CheckNums2(num1, num2):
    return num1 == num2 and "-1" or (num2 > num1 and "true" or "false")


# keep this function call here
# to see how to enter arguments in Python scroll down
print CheckNums(raw_input())
