def balance_check(s):
    if len(s) <= 1:
        return False
 
    stack = []
    closedParen = { 
        ")":"(",
        "]":"[",
        "}":"{"
    }
   
    for c in s:
        if c in closedParen:
            if stack and stack[-1] == closedParen[c]:
                stack.pop()
            else: 
                return False
        else:
            stack.append(c)
    return len(stack) == 0

print(balance_check("({[]})"))
print(balance_check("()(){}{}"))
print(balance_check(")"))
print(balance_check("({]})"))
