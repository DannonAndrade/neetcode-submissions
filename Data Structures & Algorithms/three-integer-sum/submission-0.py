class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seenTriples = set()
        twoSum = defaultdict(list)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                twoSum[ 0 - (nums[i] + nums[j])].append((i,j))

        for k in range(len(nums)):
            if nums[k] in twoSum:
                for pair in twoSum[nums[k]]:
                    if k in pair: continue
                    first = nums[pair[0]]
                    second = nums[pair[1]]
                    third = nums[k]

                    sort = tuple(sorted([first, second, third]))
                    if sort not in seenTriples:
                        res.append([first, second, third])
                        seenTriples.add(sort)


                    

                    
        return res



            
        