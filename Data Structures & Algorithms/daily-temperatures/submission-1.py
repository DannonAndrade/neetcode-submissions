class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            cur = temperatures[i]
            '''
            print("cur")
            print(cur)
            print("stack before:")
            print(stack)
            '''
            
            while stack and stack[-1][0] < cur:
                    popped = stack.pop()
                    result[popped[1]] = i - popped[1]               

            stack.append((cur,i))
            '''
            print("stack after:")
            print(stack)
            '''
        return result
                


       

            

        