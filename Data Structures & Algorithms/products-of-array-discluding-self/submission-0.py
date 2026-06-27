class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = []
        product = 1
        for i in range(len(nums)):
            pre.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] *= product
            product *= nums[i]

        
        return pre
        