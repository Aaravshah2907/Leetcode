# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        nextNode = node.next
        while nextNode.next:
            node.val = nextNode.val
            node = node.next
            nextNode = nextNode.next
        node.val = nextNode.val
        node.next = None