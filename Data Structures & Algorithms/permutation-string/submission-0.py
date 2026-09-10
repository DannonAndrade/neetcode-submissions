class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1): return False

        s1_map = defaultdict(int)
        for c in s1:
            
            s1_map[c] += 1

        counts = defaultdict(int)
        for k in range(len(s1)):
            counts[s2[k]] += 1

        if counts == s1_map: return True
        i = 0

        for j in range(len(s1), len(s2)):

            counts[s2[i]] -= 1
            if counts [s2[i]] == 0:
                del counts[s2[i]]
            counts[s2[j]] += 1
            
            i += 1
            if counts == s1_map: return True
        
        return False



        

            



        