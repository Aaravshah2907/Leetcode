# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def treegen(start,end):
            if start>end: return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = treegen(start,mid-1)
            node.right = treegen(mid + 1,end)
            return node

        return treegen(0,len(nums)-1)
        