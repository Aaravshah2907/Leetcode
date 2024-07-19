# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        temp = list1
        while count < a - 1:
            temp = temp.next
            count += 1
        temp2 = temp
        temp = temp.next
        count += 1
        temp2.next = list2
        while temp2.next:
            temp2 = temp2.next
        while count <= b :
            temp = temp.next
            count += 1
        temp2.next = temp
        return list1