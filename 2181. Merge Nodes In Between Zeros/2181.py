# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(val=0)
        pointer = head.next
        memorySaver = newHead
        while pointer.next:
            if pointer.val:
                newHead.val += pointer.val
            else:
                newNode = ListNode()
                newHead.next = newNode
                newHead = newHead.next
            pointer = pointer.next
        return memorySaver