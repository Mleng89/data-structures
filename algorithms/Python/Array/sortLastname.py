# def sortLastName(names):
#     last_name_list = []
#     for name in names:
#         person_name = name.split()
#         last_name = person_name[-1]
#         last_name_list.append(last_name)
#         sorted_by_last_name = sorted(last_name_list)
#     print(sorted_by_last_name)
def sortLastName(names):
    return sorted(names, key=lambda name: name.split()[-1])
    # names.sort(key=lambda name: name.split()[-1])
    # return names


names = [
    "Matthew Leng",
    "Eva Diep",
    "Kyle Burda",
    "Andrew Woo",
    "Edwin Li",
    "Raymond Ng",
    "Cameron Mo",
    "John Henry Smith",
]
print(sortLastName(names))
# Kyle, Eva, Edwin, Matthew, Cameron, Raymond, John, Andrew
