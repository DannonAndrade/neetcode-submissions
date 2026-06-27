class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(set(nums))
        print(sort)
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        
        chain = 1
        last = sort[0]
        ret = 1
        for i in range(1, len(sort)):
            if sort[i] - 1 == last:
                chain += 1
                ret = max(ret, chain)
            else:
                chain = 1
            last = sort[i]
        print(sort)
        return ret

