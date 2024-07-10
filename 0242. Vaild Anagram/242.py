class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = [ch for ch in t]
        for character in s:
            if character not in t_list:
                return False
            t_list.remove(character)
        return True