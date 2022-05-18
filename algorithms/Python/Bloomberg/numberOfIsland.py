"""
Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

land_count = 1 + 1 = 2
return land_count
 
[-1, 0, 0, -1] 
[-1, -1, -1, -1]
[0, 0, -1, 0]
[1, 0, -1, 0]
 o  x                
 Output: 1


# noqa
"""
from collections import deque


def travel(grid, row, column):
    DIRECTIONS = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]

    for row_movement, col_movement in DIRECTIONS:
        next_row = row + row_movement
        next_col = column + col_movement

        # check for valid movement
        # is index out of range
        # have i been there before
        is_next_row_valid = next_row >= 0 and next_row < len(grid)
        is_next_col_valid = next_col >= 0 and next_col < len(grid[row])

        if is_next_col_valid and is_next_row_valid:
            next_value = grid[next_row][next_col]

            # mark visited with -1 or -0
            # if negative in front, don't move there
            # else move
            # if 1, then continue
            # if 0, mark as visited and stop

            print(
                f"CURRENT: {(row, column)} and NEXT: {(next_row, next_col)}")

    return None


def num_of_islands(grid):
    land_count = 0
    # Loop initial list

    DIRECTIONS = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]
    # Array[2][1]
    # Array[1][1]
    visited = set()

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            current = grid[row][column]
            if current == "1" and (row, column) not in visited:
                land_count += 1
                visited.add((row, column))
                stack = [(row, column)]
                # stack = deque()
                # stack.append((row, column))
                while stack:
                    current_row, current_columm = stack.pop()

                    # print('stack, current, coordinates', stack,
                    #   grid[current_row][current_columm], [current_row, current_columm])  # noqa

                    for row_movement, col_movement in DIRECTIONS:
                        next_row = current_row + row_movement
                        next_col = current_columm + col_movement

                        # check for valid movement
                        is_next_row_valid = next_row >= 0 and next_row < len(
                            grid)
                        is_next_col_valid = next_col >= 0 and next_col < len(
                            grid[row])
                        is_not_visited = (
                            next_row, next_col) not in visited

                        if is_next_col_valid and is_next_row_valid and is_not_visited:  # noqa
                            visited.add((next_row, next_col))
                            next_value = grid[next_row][next_col]
                            if next_value == "1":
                                stack.append((next_row, next_col))

    # print("Visited set=>", visited)
    return land_count


"""
MOVEMENT TRACKER:
 - 'RR'
 - 'RDRRR'
 - 'RDRRU' # six ones ... how do we know whether we're done?
 ------
 - 'RDDLD' # we need to track where we've been to avoid extra steps like going up from RDR

grid = [
      o
    0 ["-1", "-1", "0", "-1", "0"],
     ["0", "-1", "-1", "0", "0"],
    ["-1", "-1", "0", "*1", "1"],
    ["0", "0", "0", "0", "0"]

]
"""
# Up down right left
grid = [["1", "1", "0", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "1"],
        ["0", "0", "0", "0", "0"]]
print("Solution-->", num_of_islands(grid))

"""
[
  [1]
]

- iterate over elements
- if ele = 1, stuff
- else stuff


 answer = 0
 for i in range(len(grid)):
    for j in range(len(grid[row])):
    if input[i][j] == "1":
      answer += 1
      while Something:
        check_directions and add a negative number to what you've seen.
        and while you find 1s, keep going
      # you eliminate all the "connected ones" from future iteration
  return answer
Returns 1

"""


# DFS stack --recursion (inheritly on a stack)
# BFS queue  --while loop
