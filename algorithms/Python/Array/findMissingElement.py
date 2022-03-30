"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array 
and deleting a random element. Given these two arrays, find which element is missing in the second Array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

input:
finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
output:
5 is the missing number
"""
def finder(arr1,arr2):
    # instantiate an empty dictionary/hash table
    numbers = {}
    # loop over arr2, put each item inside hashtable with value of 1, +1 if seen again later on
    for num in arr2:
        if num not in numbers:
            numbers[num] = 1
        else:
            numbers[num] += 1
    
    for num in arr1:
        if num in numbers:
            numbers[num] -= 1      
        else:
            print(f"{num} is the missing number!")
        
        if num in numbers and numbers[num] <= -1:
            print(f"{num} is the missing number!")  
        
       
    # print(numbers)
    # loop over arr1, minus 1 each time, if value is not found, return that value because it is the one taken out!

finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
finder([1,2,3,4,5,6,7,7,7], [3,7,2,1,4,6,5,7])

