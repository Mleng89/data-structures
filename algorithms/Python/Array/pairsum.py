"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

so input:
pair_sum([1,3,2,2], 4)

would return 2 pairs:

(1,3)
(2,2)
"""

# def pair_sum(arr,k):
#     # loop array with 2 pointers
#     i = arr[0]
#     j = arr[1]
#     counter = 0
#     for idx, num in enumerate(arr):
#         # print(j)
#         sum = i + j
#         if sum == k:
#             counter += 1
#         else:
#             j += 1
            
    

def pair_sum(arr, k):
    if len(arr) < 2:
        return
    
    #set for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        print('what is my target', target)
        # 3 = 4-1
        # 1 = 4-3
        # 2= 4-2
        # 2 = 4-2
        if target not in seen:
            seen.add(num)
        # seen = {1}
        # seen = {1}
        # seen = {1,2}
            print('what is my seen?', seen)

        else:
            output.add((num,target))
            # output.add(((min(num,target)), max(num,target))) # why would i need min & max...?
    # print('what is my seen?', seen)
    # print(len(output))
    print(output)

pair_sum([1,3,2,2,2, 1], 4)
# (1,3)
# (2,2)