class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(int)
        res = []

        for s in strs:
            sort = str(sorted(s))
            if sort not in hm:
                res.append([s])
                hm[sort] = len(res) - 1
            else:
                res[hm[sort]].append(s)
        
        return res
            