"""
The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character
appears only once in the original string, or ")" if that character
appears more than once in the original string. Ignore capitalization
when determining if a character is a duplicate.
"""
# UNIQUE = "("
# DUPLICATE = ")"
def duplicate_encode(word):
    UNIQUE = "("
    DUPLICATE = ")"
    lower_word = word.lower()
    result = ""
    for letter in lower_word:
        if lower_word.count(letter) == 1:
            result += UNIQUE
        else:
            result += DUPLICATE
    return result

"""
TEST CASES
"""

print(duplicate_encode('din'))  # "((("

print(duplicate_encode('recEde'))  # "()()()"

print(duplicate_encode('Success'))  # ")())())"

print(duplicate_encode('(( @'))  # "))(("

