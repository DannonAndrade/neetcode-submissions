class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers) - 1):
            compliment = target - numbers[i]

            for j in range(i + 1, len(numbers), 1):
                if numbers[j] == compliment:
                    return [i + 1,j + 1]

        return []

        