class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


def deserialize(arr):
    if len(arr) == 0:
        return None
    root = TreeNode(arr[0])
    queue = [root]

    for i in range(1, len(arr), 2):
        curr = queue.pop(0)
        if arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        if arr[i + 1] is not None:
            curr.right = TreeNode(arr[i + 1])
            queue.append(curr.right)
    return root


array = [4, 2, 5, 1, 3, None, 7, None, None, None, None, 6, 8]
treeNode = deserialize(array)
print(treeNode)


def bfs(node):
    queue = [node]
    result = []

    while len(queue) > 0:
        curr = queue.pop(0)

        result.append(curr.value)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return result


holder = []


def dfsPre(node):
    if node is None:
        return
    holder.append(node.value)
    dfsPre(node.left)
    dfsPre(node.right)

    return holder


def dfsPost(node):
    ...


def dfsIn(node):
    ...


print(bfs(treeNode))
# [4,2,5,1,3,7,6,8]
print(dfsPre(treeNode))
# [4,2,1,3,5,7,6,8]
# print(dfsIn(treeNode))
# [1,2,3,4,5,6,7,8]
# print(dfsPost(treeNode))
# [1,3,2,6,8,7,5,4]
