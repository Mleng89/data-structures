"""
You are given the heads of two sorted
linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


new_list = []


def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    print(dummy.next.val)
    print(dummy.next.next.val)
    print(dummy.next.next.next.val)
    print(dummy.next.next.next.next.val)
    print(dummy.next.next.next.next.next.val)
    return dummy.next


# 1 -> 2 -> 3
#           ^
# 1 -> 3 -> 4
#           ^

# LIST 1 START
list1_node1 = ListNode(1)
list1_node2 = ListNode(2)
list1_node3 = ListNode(4)

list1_node1.next = list1_node2
list1_node2.next = list1_node3
# LIST 1 END

# LIST 2 START
list2_node1 = ListNode(1)
list2_node2 = ListNode(3)
list2_node3 = ListNode(4)

list2_node1.next = list2_node2
list2_node3.next = list2_node3
# LIST 2 END

# ll_test1 = [1, 2, 4]
# ll_test2 = [1, 3, 4]

print(mergeTwoLists(list1_node1, list2_node1))
