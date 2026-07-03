class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        seen = set()
        max_count = 0

        for i in range(len(nums)):
            if nums[i] in seen: continue

            count = 1
            seen.add(nums[i])
            l = nums[i] - 1
            r = nums[i] + 1

            while l in seen:
                l -= 1
                count += 1
            while r in seen:
                r += 1
                count += 1
            
            max_count = max(count, max_count)

        return max_count
        