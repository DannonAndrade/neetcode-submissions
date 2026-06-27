class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = defaultdict(list)

        for s in strs:
            k = tuple(sorted(s))

            hm[k].append(s)

        return list(hm.values())


        