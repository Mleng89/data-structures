from collections import deque

from pyparsing import col
""" Candy Crush (723)
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j]
represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move.
Now, you need to restore the board to a stable state by crushing candies
according to the following rules:

    - If three or more candies of the same type are adjacent vertically or horizontally,
      crush them all at the same time - these positions become empty.
    - After crushing all candies simultaneously, if an empty space on the board has candies on top of itself,
      then these candies will drop until they hit a candy or bottom at the same time; no new candies will drop outside the top boundary.
    - After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
    - If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the stable board.

EXAMPLE
INPUT:
 board = [
    [110, 5, 112, 113, 114],
    [210, 211, 5, 213, 214],
    [310, 311, 3, 313, 314],
    [410, 411, 412, 5, 414],
    [5, 1, 512, 3, 3],
    [610, 4, 1, 613, 614],
    [710, 1, 2, 713, 714],
    [810, 1, 2, 1, 1],
    [1, 1, 2, 2, 2],
    [4, 1, 4, 4, 1014],
]
OUTPUT:
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [110, 0, 0, 0, 114],
    [210, 0, 0, 0, 214],
    [310, 0, 0, 113, 314],
    [410, 0, 0, 213, 414],
    [610, 211, 112, 313, 614],
    [710, 311, 412, 613, 714],
    [810, 411, 512, 713, 1014],
]
# noqa
"""

"""
NOTES:
Grid of MxN
board[i][j] is type of candy
board[i][j] === 0 cell is empty

M >= 3
N <= 50

[
>[1, 1, 1, 2, 2]
  ^
[4, 1, 4, 4, 1014]
    ^
[11,1,5,4,7]
    ^
]



val, r, c, prev_val = stack.pop()

board[r][c] = prev_val

Stack:
"""


# def candyCrush(board):
# Error handle
# if not board:
#     return board

# done = True

# for row in range(len(board)):

#     for column in range(len(board[row])-2):
#         print('column', board[column])
#         num1 = abs(board[row][column])
#         num2 = abs(board[row][column+1])
#         num3 = abs(board[row][column+2])

#         if num1 == num2 and num2 == num3 and num1 != 0:
#             board[row][column] = -num1
#             board[row][column + 1] = -num2
#             board[row][column+2] = -num3
#             done = False
# for column in range(len(board[0])):
#     for row in range(len(board) - 2):
#         num1 = abs(board[row][column])
#         num2 = abs(board[row + 1][column])
#         num3 = abs(board[row + 2][column])
#         if num1 == num2 and num2 == num3 and num1 != 0:
#             board[row][column] = -num1
#             board[row + 1][column] = -num2
#             board[row + 2][column] = -num3
#             done = False
# if not done:
#     for column in range(len(board[0])):
#         index = len(board) - 1
#         for row in range(len(board)-1, -1, -1):
#             if board[row][column] > 0:
#                 board[index][column] = board[row][column]
#                 index -= 1
#             for row in range(index, -1, -1):
#                 board[row][column] = 0

# return board

def candyCrush(board):

    R, C = len(board), len(board[0])
    changed = True

    while changed:
        changed = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:  # noqa
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])  # noqa
                    changed = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:  # noqa
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])  # noqa
                    changed = True

        for c in range(C):
            i = R-1
            for r in reversed(range(R)):
                if board[r][c] > 0:
                    board[i][c] = board[r][c]
                    i -= 1
            for r in reversed(range(i+1)):
                board[r][c] = 0
    return board


# def candyCrush(board):
#     row_num, column_num = len(board), len(board[0])
#     done = True
#     while done:
#         done = False

#         for row in range(row_num):
#             for column in range(column_num - 2):
#                 if abs(board[row][column]) == abs(board[row][column+1]) == abs(board[row][column+2]) != 0:  # noqa
#                     board[row][column] = board[row][column + 1] = board[row][column+2] = -abs(board[row][column])  # noqa
#                     done = True
#         for row in range(row_num - 2):
#             for column in range(column_num):
#                 if abs(board[row][column] == abs(board[row+1][column]) == abs(board[row+2][column]) != 0):  # noqa
#                     board[row][column] = board[row+1][column] = board[row+2][column] = -abs(board[row][column])  # noqa
#                     done = True
#         for column in range(column_num):
#             index = row_num - 1

#             for row in reversed(range(row_num)):
#                 if board[row][column] > 0:
#                     board[index][column] = board[row][column]
#                     index -= 1
#             for row in reversed(range(index+1)):
#                 board[row][column] = 0

#     return board

board = [

        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
]


print(candyCrush(board))
