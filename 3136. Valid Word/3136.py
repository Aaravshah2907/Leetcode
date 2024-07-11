class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e','i','o','u','A', 'E','I','O','U']
        VOW_COUNT = 0
        NUM_COUNT = 0
        if len(word) >= 3:
            for character in word:
                if character.isalnum():
                    if character.isnumeric():
                        NUM_COUNT += 1
                    if character in vowels:
                        VOW_COUNT += 1
                else:
                    return False
            if (len(word) - NUM_COUNT - VOW_COUNT) >= 1 and VOW_COUNT:
                return True
            else:
                return False
        else:
            return False