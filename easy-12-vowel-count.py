# Have the function VowelCount(str) take the str string parameter being passed
# and return the number of vowels the string contains (ie. "All cows eat grass"
# would return 5). Do not count y as a vowel for this challenge.


def VowelCount(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([ch for ch in str_ if ch.lower() in vowels])


def VowelCount2(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels = "aeiou"
    return len(filter(lambda x: x.lower() in vowels, str_))


# keep this function call here
# to see how to enter arguments in Python scroll down
print VowelCount(raw_input())
