def two_sum(arr, target):
    hash = {}
    for index, num in enumerate(arr):
        diff = target - num
        print("mydiff", diff)
        if diff in hash:
            print(hash[diff], index)
        hash[num] = index

    print(hash)


two_sum([2, 7, 11, 15], 9)

# [2,7,11,15]
# 9
