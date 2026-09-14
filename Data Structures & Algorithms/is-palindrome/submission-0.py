class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        r = ""

        for char in s:
            if(char != " " and char.isalnum()):
                r = char.lower() + r
        
        return r == r[::-1]