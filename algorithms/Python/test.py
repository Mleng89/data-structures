# obj = {
#     'NSG': {
#         'name': 'NNSSP',
#         'position': 3
#     },
#     'CAB': {
#         'name': 'CBSSP',
#         'position': 2
#     },
#     'EQU': {
#         "name": 'SSP',
#         "position": 1
#     }
# }


# def sort_by_name(input: dict) -> dict:
#     # sorted([])
#     # list.sort() // input.sort()
#     # print(input.items())
#     """
#     [
#       ('CAB', {'name': 'CBSSP', 'position': 2})
#       ('NSG', {'name': 'NNSSP', 'position': 3})
#       ('EQU', {'name': 'SSP', 'position': 1})
#     ]
#     """
#     # x = list(input.items())
#     # x.sort(key=lambda kvs: kvs[1]['name'])
#     # return dict(x)
#     return dict(sorted(input.items(), key=lambda kvs: kvs[1]['name']))


# print(sort_by_name(obj))
from collections import deque

graph = {}
graph["matt"] = ["andrew", "ray", "edwin"]
graph["andrew"] = ["kaye", "brandon"]
graph["ray"] = ["anthony", "andy", "tommy"]
graph["edwin"] = ["sujata", "samson", "boris"]
graph["kaye"] = ["kelly"]
graph["brandon"] = []
graph["anthony"] = []
graph["andy"] = []
graph["tommy"] = []
graph['sujata'] = []
graph["samson"] = []
graph['boris'] = []


def name_is_true(name):
    return name[-1] == 'a'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if name_is_true(person):
                print(f"{person} has an a at the end of their name!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                print(searched)
    return False


print(search('matt'))
