class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0
        buy = float("inf")
        buy_idx = -1


        for i in range(len(prices)):

            if prices[i] - buy > max_prof:
                print(buy)
                print(prices[i])
                max_prof = prices[i] - buy
                
                print(max_prof)


            if prices[i] < buy:
                buy_idx = i
                buy = prices[i]
            
        return max_prof



        