class Solution:

    def reverse(self, x: int) -> int:
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return reversed_num

    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        if self.reverse(x) != x:
            return False
        
        return True