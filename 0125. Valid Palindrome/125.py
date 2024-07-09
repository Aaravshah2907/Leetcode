class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        if len(s) == 0:
            return True
        char = []
        for ch in s:
            if ch.isalnum():
                char.append(ch)
        for x,ch in enumerate(char):
            if ch != char[len(char) -1-x]:
                return False
        return True