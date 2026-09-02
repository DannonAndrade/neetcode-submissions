class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = []
        hm = defaultdict(list)

        for s in strs:
            hm[tuple(sorted(s))].append(s)

        return list(hm.values())
            

        