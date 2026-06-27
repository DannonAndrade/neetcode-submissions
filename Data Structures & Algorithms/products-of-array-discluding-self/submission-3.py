class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)

        total_product = 1
        zero_idx = -1


        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
            elif zero_idx == -1:
                zero_idx = i
            else:
                return output

        if zero_idx != -1:
            output[zero_idx] = total_product
            return output

        for i in range(len(nums)):
                output[i] = total_product // nums[i]

        return output

