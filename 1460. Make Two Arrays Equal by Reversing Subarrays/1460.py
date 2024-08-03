class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for index in range(len(arr)):
            if target[index] != arr[index]:
                return False
        return True