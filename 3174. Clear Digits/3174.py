class Solution:
    def clearDigits(self, s: str) -> str:
        chars = []
        for ch in s:
            if ch.isdigit():
                chars.pop()
            else:
                chars.append(ch)
        return "".join(chars)