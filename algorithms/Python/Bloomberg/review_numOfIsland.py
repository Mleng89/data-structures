"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","1","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]
Output: 1

Stack: (1,0)  (2,1)

# noqa
"""
"""
Notes:
*** Input is an array of arrys of strings
0)
variable to track number of islands - integer = 0

1)
Directions: Right, Down, Left, Up
Right - grid[row][column + 1]
Down - grid[row + 1][column]
Left - grid[row][column - 1]
Up - grid[row - 1][column]

2)
Marking Values visited. -- Graph Cycle (look up term)
    - if visited, turn string value to "V"
**Cannot move on: Out of bounds & 0 / Visited

stack - DFS
queue - BFS
"""

# Out of bounds: negative index, index is past len(list)


def numIsland(grid: list[list[str]]) -> int:
    directions = {
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "up": (-1, 0)
    }
    islands = 0
    stack = []
    #[ (0,0), (0,1), (1,0), (0,2), (0,3), (1,3), (1,1), (2,0), (2,1) ]
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "1":

                grid[row][column] = "V"
                stack.append((row, column))
                # Start DFS
                while stack:
                    current = stack.pop()
                # peeking logic:
                # is my directions[right] == "1"?
                # if it is a "1"

                islands = islands + 1
                # pop every out of my stack
            if grid[row][column] == "0":
                grid[row][column] = "V"

    return islands


# islands = 1
grid = [
    ["1v", "1v", "1v", "1v", "0v"],
    ["1v", "1v", "0v", "1v", "0v"],
    ["1v", "1v", "0v", "0v", "0"],
    ["0v", "0v", "0", "0", "0"]
]


print(numIsland(grid))
