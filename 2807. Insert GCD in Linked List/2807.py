# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head 
        def gcf(a,b):
            while b !=0:
                a,b = b,a%b
            return a
        while head and head.next:
            head.next = ListNode(gcf(head.val,head.next.val),head.next)
            head = head.next.next
        return pointer