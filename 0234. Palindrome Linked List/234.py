# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr) - i -1]:
                return False
        return True