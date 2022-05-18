obj = {
    'NSG': {
        'name': 'NNSSP',
        'position': 3
    },
    'CAB': {
        'name': 'CBSSP',
        'position': 2
    },
    'EQU': {
        "name": 'SSP',
        "position": 1
    }
}


def sort_by_name(input: dict) -> dict:
    # sorted([])
    # list.sort() // input.sort()
    # print(input.items())
    """
    [
      ('CAB', {'name': 'CBSSP', 'position': 2})
      ('NSG', {'name': 'NNSSP', 'position': 3})
      ('EQU', {'name': 'SSP', 'position': 1})
    ]
    """
    # x = list(input.items())
    # x.sort(key=lambda kvs: kvs[1]['name'])
    # return dict(x)
    return dict(sorted(input.items(), key=lambda kvs: kvs[1]['name']))


print(sort_by_name(obj))
