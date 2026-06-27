class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = []
        i = 0
        while len(strs) > 0:
            s = strs.pop(0)
            groups.append([s])
            s_count = Counter(s)

            j = 0
            while j < len(strs):
                if Counter(strs[j]) == s_count:
                    groups[i].append(strs.pop(j))
                else:
                    j += 1
            i += 1
            
        return groups


        