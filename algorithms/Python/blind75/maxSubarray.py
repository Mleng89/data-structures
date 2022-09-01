def maxSubArray(nums) -> int:
    maxTotal = 0
    for index in range(len(nums)):
        length = len(nums)
        if index >= length:
            return
        # num = nums[index]
        # nextNum = nums[index+1]
        # total = num + nextNum
        if total > maxTotal:
            maxTotal = total

    return maxTotal


print(maxSubArray([1, 1, -2]))  # expected 2
