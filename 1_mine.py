class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_nums = len(nums)
        for length in range(length_nums):
            for element in range(length + 1, length_nums):
                if nums[length] + nums[element] == target:
                    return [element, length]