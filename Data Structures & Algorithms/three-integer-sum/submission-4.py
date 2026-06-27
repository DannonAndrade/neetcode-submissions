class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            compliment = 0 - nums[i]

            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                summation = nums[j] + nums[k]
                if summation == compliment:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif summation < compliment:
                    j += 1
                elif summation > compliment:
                    k -= 1
        return res

        
                 

