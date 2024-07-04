class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for customers in accounts:
            sum = 0
            for banks in customers:
                sum += banks
            if sum > maxwealth:
                maxwealth = sum
        return maxwealth