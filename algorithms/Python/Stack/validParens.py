"""
Given a string s containing just the
characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


def isValid(s):
    open_and_closed = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    for char in s:
        if char in open_and_closed:
            if stack and stack[-1] == open_and_closed[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True


print(isValid("["))
