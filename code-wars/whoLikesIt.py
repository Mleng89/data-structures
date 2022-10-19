def likes(names):
    result = ""
    if len(names) == 0:
        result = "no one likes this"
    elif len(names) == 1:
        result = str(names[0]) + " likes this"
    elif len(names) > 1 and len(names) < 4:
        for name in range(0, len(names) - 1):
            result = result + names[name] + ", "
        result = result[:-2]
        result = result + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            result = result + names[name] + ", "
        result = result[:-2]
        result = result + " and " + str(len(names) - 2) + " others like this"
    return result


"""
Tests
"""
print(likes([]))  #'no one likes this'
print(likes(["Peter"]))  # 'Peter likes this'
print(likes(["Jacob", "Alex"]))  # 'Jacob and Alex like this'
print(likes(["Max", "John", "Mark"]))  # 'Max, John and Mark like this'
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # 'Alex, Jacob and 2 others like this'
