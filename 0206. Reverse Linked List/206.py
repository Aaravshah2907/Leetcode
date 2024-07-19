# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        NodesArray = []
        temp = head
        val = temp.val
        while temp:
            NodesArray.append(temp)
            val = temp.val
            temp = temp.next
        newHead = NodesArray[-1]
        for index in range(len(NodesArray)-2,-1,-1):
            newHead.next = NodesArray[index]
            newHead = newHead.next
        newHead.next = None
        return NodesArray[-1]