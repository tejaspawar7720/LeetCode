class Solution:
    def isPalindrome(self, x):
        num = x
        reverse = 0
        temp = x

        while temp > 0:
            last_digit = temp %  10
            reverse  = reverse * 10 + last_digit
            temp = temp // 10
        
        if num == reverse:
            return True
        else:
            return False
        