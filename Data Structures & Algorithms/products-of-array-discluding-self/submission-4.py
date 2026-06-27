class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [1] * len(nums)

        for i in range(1, len(nums), 1):
            left[i] = nums[i - 1] * left[i - 1]
            right[len(nums) - 1 - i] = nums[len(nums) - i] * right[len(nums) - i]

        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output
