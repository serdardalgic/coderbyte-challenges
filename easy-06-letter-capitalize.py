# Have the function LetterCapitalize(str) take the str parameter being passed
# and capitalize the first letter of each word. Words will be separated by only
# one space.


def LetterCapitalize(str):
    return " ".join(word.capitalize() for word in str.split())


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCapitalize(raw_input())
