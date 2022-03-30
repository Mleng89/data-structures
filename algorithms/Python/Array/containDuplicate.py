"""
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

"""
# Hash table solution

def containsDuplicate(nums):
    dupe_list = {}
    for num in nums:
        if num not in dupe_list:
            dupe_list[num] = 1
        else:
            print(True)
            print(f"This number is dupe {num}")
            return True
    print(False)
    return False
"""        
    
def containsDuplicate(nums):
    num_set = set(nums)
    if len(nums) == len(num_set):
        print(False)
        return False
    print(True)
    return True
containsDuplicate([1,2,3,1]) # True
containsDuplicate([1,2,3,4]) # False
# containsDuplicate([]) # False