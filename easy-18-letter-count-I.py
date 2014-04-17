# Have the function LetterCountI(str) take the str parameter being passed and
# return the first word with the greatest number of repeated letters. For
# example: "Today, is the greatest day ever!" should return greatest because it
# has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there
# are no words with repeating letters return -1. Words will be separated by
# spaces.


def LetterCount(str_):
    #str = str.lower()
    maxlt_word = None
    max_lts = [(0, '')]
    for word in str_.split():
        if len(word) == len(set(word)):
            continue
        letter_list = [(word.count(letter), letter) for letter in set(word)]
        max_of_lt = max(letter_list)[0]
        if max_of_lt > 1:
            word_max_lts = filter(
                lambda x: x[0] == max(letter_list)[0], letter_list)
            if max(word_max_lts)[0] > max(max_lts)[0]:
                maxlt_word = word
                max_lts = word_max_lts
            if max(word_max_lts)[0] == max(max_lts)[0]:
                if len(word_max_lts) > len(max_lts):
                    maxlt_word = word
                    max_lts = word_max_lts

    return maxlt_word or -1


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCount(raw_input())
