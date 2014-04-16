# Have the function SimpleSymbols(str) take the str parameter being passed and
# determine if it is an acceptable sequence by either returning the string true
# or false. The str parameter will be composed of + and = symbols with several
# letters between them (ie. ++d+===+c++==a) and for the string to be true each
# letter must be surrounded by a + symbol. So the string to the left would be
# false. The string will not be empty and will have at least one letter.


def SimpleSymbols(str):
    prev = ""
    in_cmp = False
    for ch in str:
        if ch.isalpha():
            if prev != "+":
                return 'false'
            in_cmp = True
        elif prev.isalpha():
            if ch != '+':
                return 'false'
            in_cmp = False
        prev = ch
    return 'false' if in_cmp else 'true'
    # Same return expression written with and/or logic
    #return in_cmp and 'false' or 'true'


# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())
