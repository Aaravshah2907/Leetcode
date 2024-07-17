# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = -1
        itr = head
        while itr:
            count += 1
            itr = itr.next
        pointer = head
        number = 0
        while pointer:
            number += ((2**count)*pointer.val)
            count -= 1
            pointer = pointer.next
        return number