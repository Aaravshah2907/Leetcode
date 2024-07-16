class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = {}
        for num in nums:
            if num in hashset:
                hashset[num] += 1
            else:
                hashset.update({num:1})
        keys = hashset.keys()
        for key in keys:
            if hashset[key] > len(nums)//2:
                return key