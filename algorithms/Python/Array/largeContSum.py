"""
Given an array of integers (positive & negative) find the largest continuous sum.

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
"""

def large_cont_sum(arr):
    if len(arr) == 0:
        return
    sum = 0
    for num in arr:
        sum += num
        new_sum = sum
        if new_sum > sum:
            sum = new_sum
        
        print(sum)

large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) 
# 29
    