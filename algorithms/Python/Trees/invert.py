"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

# Definition for a binary tree node.


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"[{self.val}, {self.left}, {self.right}]"


def deserialize(arr):
    if len(arr) == 0:
        return None
    root = Tree(arr[0])
    queue = [root]

    for i in range(1, len(arr), 2):
        curr = queue.pop(0)
        if arr[i] is not None:
            curr.left = Tree(arr[i])
            queue.append(curr.left)
        if arr[i + 1] is not None:
            curr.right = Tree(arr[i + 1])
            queue.append(curr.right)
    return root


def invertTree(root):
    if root is None:
        return
    invertTree(root.left)
    invertTree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

    return root


array = [4, 2, 7, 1, 3, 6, 9]
# [4,7,2,9,6,3,1]
tree = deserialize(array)
print('tree looks like:', tree)
print(invertTree(tree))
