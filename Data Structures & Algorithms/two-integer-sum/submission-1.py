class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = defaultdict(int)
        for i in range(len(nums)):
            pair = target - nums[i]

            if pair in hm:
                return [hm[pair], i]
            elif nums[i] not in hm:
                hm[nums[i]] = i 
