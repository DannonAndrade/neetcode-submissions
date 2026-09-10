class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        
        if need == window: return True

        l = 0
        
        for r in range(len(s1), len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if need == window: return True
        
        return False


        
        
