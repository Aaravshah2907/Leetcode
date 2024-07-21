# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        max, l = 0, len(arr)
        for index in range(l//2):
            if max < arr[index] + arr[l - index -1]:
                max = arr[index] + arr[l - index -1]
        return max