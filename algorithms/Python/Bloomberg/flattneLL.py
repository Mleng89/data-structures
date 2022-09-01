"""
[1] -> [2] -> [11] -> [8] -> [10]
                |      |
                |      [9]
                |
                [4] -> [5] -> [6]
                               |
                            [7]

[1] -> [2] -> [11] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9] -> [10]

"""

# INPUT: head of LL
#OUTPUT: LL in place


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None


# merge List
# if down node exist, want to insert into node that has the .down

def mergeList(node):
    while node.data:
        if node.down is None:
            node.next
        elif node.down:
            temp1 = node.next
            temp2 = node.down
            node.next = temp2
            node.next = temp1
