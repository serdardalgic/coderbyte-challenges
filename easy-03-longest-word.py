# Have the function LongestWord(sen) take the sen parameter being passed and
# return the largest word in the string. If there are two or more words that
# are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.


def LongestWord(sen):
    longest = ""
    for word in sen.split():
        if word.isalpha():
            #if re.match('^[\w-]+$', word):
            longest = word if len(word) > len(longest) else longest
    return longest


def LongestWord2(sen):
    return max(filter(lambda x: x.isalpha(), sen.split()), key=len)


# keep this function call here
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())
