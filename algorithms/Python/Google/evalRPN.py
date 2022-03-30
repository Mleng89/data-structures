"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or
another expression. Note that division between two integers should
truncate toward zero.

It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result,
and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


def evalRPN(tokens):
    if len(tokens) <= 2:
        return None
    total = None
    temp = []

    def applyOperator(operator, nums, total):
        if operator == "+":
            total += nums
        if operator == "*":
            total *= nums
        if operator == "/":
            total /= nums
        if operator == "-":
            total -= nums

    operators = {"+", "-", "/", "*"}

    # total = None
    # switch = False
    for ele in tokens:
        if total is None and ele not in operators:
            total = int(ele)
        elif len(temp) >= 0 and ele not in operators:
            temp.append(int(ele))
        if ele in operators:
            applyOperator(ele, total)
            temp = []
        print("temp", temp)
    return total


test = ["2", "1", "+", "3", "*"]
# total = 2
# test [1,+,3,*]
# evalRPN(test)

########


def applyOperator(operator, nums):
    if operator == "+":
        return nums[0] + nums[1]
    if operator == "*":
        return nums[0] * nums[1]
    if operator == "/":
        return nums[0] / nums[1]
    if operator == "-":
        return nums[0] - nums[1]


def _evalRPN(tokens):
    if len(tokens) <= 2:
        return None
    running_total = []

    operators = {"+", "-", "/", "*"}

    for num_or_op_as_str in tokens:
        if len(running_total) >= 0 and num_or_op_as_str not in operators:
            running_total.append(int(num_or_op_as_str))
        if num_or_op_as_str in operators:
            current_length_of_running_total = len(running_total)

            num1 = int(running_total[current_length_of_running_total - 2])
            num2 = int(running_total[current_length_of_running_total - 1])
            # ! remove num1 and num2 from running_total array,
            # ! then, replace that section of array with below data
            # [3]
            # [1::]
            # [::3]
            # [1:3]
            running_total.append(applyOperator(num_or_op_as_str, [num1, num2]))

    return running_total  # TODO: extract int from array


_test = ["2", "1", "+", "3", "*"]
print("solution", _evalRPN(_test))


# def fun():
#     greet = "hello"
#     return greet


# print(type(fun()))


# except ValueError:
#     print("what is:", ele, expression, total)
#     if total is None and ele in operators:
#         if ele == "+":
#             total = expression[0] + expression[1]

#         if ele == "*":
#             total = expression[0] * expression[1]

#         if ele == "/":
#             total = expression[0] / expression[1]

#         if ele == "-":
#             total = expression[0] - expression[1]
#         expression = []

#     elif total is not None and ele in operators:
#         if ele == "+":
#             total += expression[0]

#         if ele == "*":
#             total *= expression[0]

#         if ele == "/":
#             total /= expression[0]

#         if ele == "-":
#             total -= expression[0]
#         expression = []
#     else:
#         print(f"There has been an error: {ValueError}")
#         print(ele)
