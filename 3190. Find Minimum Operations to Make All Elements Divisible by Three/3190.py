class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = len(nums)
        for num in nums:
            if num%3 == 0:
                count -= 1
        return count