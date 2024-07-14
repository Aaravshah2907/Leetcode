class Solution:
    def reverseString(self, s: List[str]) -> None:
        for index in range(len(s)//2):
            char = s[index]
            s[index] = s[len(s) - index - 1]
            s[len(s) - index - 1] = char