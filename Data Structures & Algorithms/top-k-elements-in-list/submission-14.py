class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = defaultdict(int)
        arr = [[] for i in range(len(nums) + 1)]
        out = []

        for n in nums:
            hm[n] += 1
        
        for n, c in hm.items():
            arr[c].append(n)
        
        for i in range(len(arr) - 1, -1, -1):
            for j in range(len(arr[i])):
                out.append(arr[i][j])
                if len(out) == k: 
                    return out
        
        return out
            
