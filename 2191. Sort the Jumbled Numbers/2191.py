class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            if not num:
                return mapping[0]
            sum, ind = 0, 0
            while num:
                dig,num = num%10, num//10
                sum += mapping[dig]*(10**ind)
                ind += 1
            return sum
        indices = sorted(range(len(nums)), key= lambda i: convert(nums[i]))
        return [nums[i] for i in indices]