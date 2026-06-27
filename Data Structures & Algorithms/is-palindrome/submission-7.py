class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0 
        j = len(s) - 1

        while i < j:
            while s[i].isalnum() == False and i < len(s) - 1:
                i += 1
            while s[j].isalnum() == False and j > 0:
                j -= 1
            
            if s[i].casefold() != s[j].casefold():
                if(i < j):
                    return False

            i += 1
            j -= 1

        return True
        