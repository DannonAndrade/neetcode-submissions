class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hs = set(nums)
        seen = set()
        max_count = 0

        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            
            count = 1
            seen.add(nums[i])
            l = nums[i] - 1
            r = nums[i] + 1

            while l in hs:
                count += 1
                seen.add(l)
                l -= 1
                
            while r in hs:
                count += 1
                seen.add(r)
                r += 1

            max_count = max(max_count, count)
        return max_count


