class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        maxElement = max(nums)
        minValue = 10 ** 4 
        for num in range(maxElement,-minValue-1,-1):
            k -= freq[num]
            if k <=0 : return num    