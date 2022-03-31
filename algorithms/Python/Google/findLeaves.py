"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
    Collect all the leaf nodes.
    Remove all the leaf nodes.
    Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5] |

Output: [[4,5,3],[2],[1]]

Explanation: 
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers
since per each level it does not matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]
"""

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        # self.children = []

    def __str__(self):
        return f"[{self.value}, {self.left}, {self.right}]"
        # return f"TreeNode(value={self.value}, left={self.left}, right={self.right})"

    # def add_children(self, child_node):
    #     print(f"Adding {child_node.value}")
    #     self.children_append(child_node)

    # def remove_child(self, child_node):
    #     print(f"Removing {child_node.value} from {self.value}")
    #     self.children = [child for child in self.children if child is not child_node]


def findLeaves(root):
    ans = []
    tmp_leaves = []
    prev_parent = None

    COUNT = 0

    def dfs(node):
        if node is None:
            return None

        # node.value = 2, node.left.value = 4
        left_node, right_node = None, None
        if node.left is not None:
            left_node = dfs(node.left)

        if node.right is not None:
            right_node = dfs(node.right)

        if left_node is None and right_node is None:
            tmp_leaves.append(node.value)
            return node

        if right_node and right_node.left is None and right_node.right is None:
            print("count", COUNT)
            print(f"REMOVE {right_node} from", node.value)
            node.left = None
            node.right = None
        if left_node and left_node.left is None and left_node.right is None:
            print("count", COUNT)
            print(f"REMOVE {left_node} from", node.value)
            node.left = None
            node.right = None

        # assumes values of nodes are unique
        # if len(tmp_leaves) > 0:
        #     if node.left and node.left.value in tmp_leaves:
        #         node.left = None
        #     if node.right and node.right.value in tmp_leaves:
        #         node.right = None
        return node

    # print("ROOT -->", root)
    dfs(root)
    # while COUNT < 2 or root.left or root.right:
    #     dfs(root)
    #     ans.append(tmp_leaves)
    #     tmp_leaves = []
    #     COUNT+=1
    ans.append(tmp_leaves)
    ans.append([root.value])
    return ans


"""
[1, [2, [4, [6 [], 10], [11, [1, 4]]], [5, None, None]], [3, None, None]]
[1, [2, [4, [8, None, None], None], [5, None, None]], [3, [6, None, None], [7, None, None]]]

"""
## TEST - EXAMPLE 1 - HARDCODED
test_tree_root = TreeNode(1)
test_tree_node2 = TreeNode(2)
test_tree_node3 = TreeNode(3)
test_tree_node4 = TreeNode(4)
test_tree_node5 = TreeNode(5)
# test_tree_node6 = TreeNode(6)
# test_tree_node7 = TreeNode(7)
# test_tree_node8 = TreeNode(8)

test_tree_root.left = test_tree_node2
test_tree_root.right = test_tree_node3

test_tree_node2.left = test_tree_node4
test_tree_node2.right = test_tree_node5
# test_tree_node3.left = test_tree_node6
# test_tree_node3.right = test_tree_node7
# test_tree_node4.left=test_tree_node8


print("Solution ->", findLeaves(test_tree_root))
## END - EXAMPLE 1
