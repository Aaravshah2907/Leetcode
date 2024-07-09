class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(' ')
        length = 0
        for char in words[-1]:
            length += 1
        return length