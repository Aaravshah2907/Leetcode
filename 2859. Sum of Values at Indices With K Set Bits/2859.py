class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for index,num in enumerate(nums):
            if bin(index).count("1") == k:
                sum += num
        return sum