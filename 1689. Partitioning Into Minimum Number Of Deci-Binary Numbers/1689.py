class Solution:
    def minPartitions(self, n: str) -> int:
        maxDig = 0
        for char in n:
            if int(char) > maxDig:
                maxDig = int(char)
        return maxDig
