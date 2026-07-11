class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = abs(x)
        result = 0
        

        while num>0:
            ld = num%10
            result = (result*10)+ld
            num = num//10
        if(result == x):
            return True
        else:
            return False
            