class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hm:
                return [hm[complement],i]
            if nums[i] not in hm:
                hm[nums[i]] = i
            
            
        return []

        