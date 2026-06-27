class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            counts[n] += 1

        for n,c in counts.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

        return res


        