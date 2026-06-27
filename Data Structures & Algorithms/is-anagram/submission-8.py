class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count = defaultdict(int)
        for c in s:
            Count[c] += 1
        
        for c in t:
            if c not in Count:
                return False
            Count[c] -= 1

            if Count[c] == 0:
                del Count[c]
        
        return not Count

