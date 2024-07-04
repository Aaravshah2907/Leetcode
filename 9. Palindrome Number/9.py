class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_str = str(x)
        len_number = len(number_str)
        for index in range(len_number//2):
            if number_str[index] != number_str[len_number - 1 - index]:
                return False
        return True