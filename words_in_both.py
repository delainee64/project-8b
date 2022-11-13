# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/11/2022
# Description: Write a function named words_in_both that takes two
# strings as parameters and returns a set of only those words that appear in both strings.

def words_in_both(string_1, string_2):
    """Takes two strings of words and returns only the words that appear in both strings."""
    words_in_1 = string_1.lower().split(" ")
    words_in_2 = string_2.lower().split(" ")
    result = set()
    for word in words_in_1:
        """for loop runs through words in (1) to find the same word in (2) """
        if word in words_in_2:
            result.add(word)
    return result


# print(words_in_both("She is a jaCK of all trades", 'Jack was tallest OF all.'))
