class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vow_list = [vowel for vowel in s if vowel in vowels]
        vow_list.sort()
        index = 0
        new_str = ""
        for ch in s:
            if ch in vowels:
                new_str += vow_list[index]
                index += 1
            else:
                new_str += ch
        return new_str 