class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            groups[key].append(strs[i])

        return list(groups.values())