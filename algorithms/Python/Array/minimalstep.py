"""
Given an array of ints num, start with an 
initial positive value start_value

In each iteration, you can calculate the 
step by step sum of start_value plus 
elements in nums (from left to right)

Return the minimum positive value of 
start_value such that the step by 
step is never less than 1

Example:
Input: nums = [-3, 2, -3, 4, 2]

Output: 5
Explination: If you choose start_value = 4, 
in the third iteration your step by 
step sum is less than 1 and step by step sum

start_value = 4 | start_value = 5 | nums
(4 -3)          |   (5 -3) = 2    | -3
(1 +2)          |   (2 +2) = 4    |  2
(3 -3)          |   (4 -3) = 1    | -3
(0 +4)          |   (1 +4) = 5    | 4
(4 +2)          |   (5 +2) = 7    | 2


Example 2: 
Input: nums = [1,2]

output: 1
Explination: Minimum start value should be positive


Example 3:
Input = nums = [1,2,-3]
Output: 5
"""

def min_start_value(nums):
    # steps = float('inf')
    steps = 0
    sum = 0
    for i in nums:
        sum += i
        steps = min(sum,steps)
    # print(-steps +1)
    print(abs(1-steps))
        

min_start_value([-3,2,-3,4,2]) # 5
min_start_value([1,2])
min_start_value([1,-2,-3])