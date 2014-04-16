# Have the function LetterChanges(str) take the str parameter being passed and
# modify it using the following algorithm. Replace every letter in the string
# with the letter following it in the alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally
# return this modified string.


def LetterChanges(stre):
    rv_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in stre:
        if ord('a') <= ord(letter) and ord(letter) < ord('z'):
            ch_str = ord(letter) + 1
            if ch_str in map(ord, vowels):
                rv_str += chr(ch_str - 32)
            else:
                rv_str += chr(ch_str)
        elif letter == 'z':
            rv_str += 'A'
        else:
            rv_str += letter
    return rv_str


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())
