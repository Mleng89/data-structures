"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that the original data
does not contain any digits and that digits are only for those repeat numbers, k.

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""
# def decodeString(s: str) -> str:
#     stack: list[str] = []

#     for i in range(len(s)):
#         if s[i] != "]":
#             stack.append(s[i])
#             print('stack:', stack)
#         else:
#             substr = ""
#             while stack[-1] != "[":
#                 substr = stack.pop() + substr
#                 print('substr:', substr)
#             stack.pop()  # to pop opening bracket

#             k = ""
#             while stack and stack[-1].isdigit():
#                 k = stack.pop() + k
#                 print('k:', k)

#             stack.append(substr*int(k))
#     return "".join(stack)


def decodeString(s: str) -> str:
    stack: list[str] = []
    for idx in range(len(s)):
        if s[idx] != "]":
            stack.append(s[idx])
        else:
            new_string = ""
            while stack[-1] != "[":
                new_string = stack.pop() + new_string
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(new_string*int(k))

    return "".join(stack)


print(decodeString("3[a2[c]]"))

"""
Input: s = "3[a]2[bc]"

Output: "aaabcbc

Stack : 3, [, a, 2, [, c
new_str = "a"
"""
"""
stack = []
        # res = ""
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() #to pop opening bracket

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(substr*int(k))

        return "".join(stack)
"""