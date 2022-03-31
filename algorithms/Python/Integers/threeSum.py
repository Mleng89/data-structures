"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def threeSum(nums):
    # i =/= j, i=/= k, j=/=k
    # nums[i] + nums[k], nums[k] == 0
    # 3 pointers?
    for index, num in enumerate(nums):
        print(f"index: {index}, num: {num}")


test_nums = [-1, 0, 1, 2, -1, -4]
# [[-1,-1,2], [-1,0,1]]
threeSum(test_nums)
