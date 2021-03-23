class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0 
        min_index, max_index =0, 0
        for i in range(1, len(prices)):
            if prices[min_index] > prices[i]:
                min_index = i
            if prices[max_index] < prices[i]:
                max_index = i
            if max_index > min_index:
                max_profit += prices[max_index] - prices[min_index]
                min_index = max_index
            else:
                max_index = min_index
        return max_profit
