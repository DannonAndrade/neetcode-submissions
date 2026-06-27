class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = defaultdict(int)
        tmap = defaultdict(int)
        
        for n in s:
            smap[n] += 1
        for x in t:
            tmap[x] += 1

        return smap == tmap