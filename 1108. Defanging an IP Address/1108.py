class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = ""
        for ch in address:
            if ch == '.':
                string += "[.]"
            else:
                string += ch
        return string