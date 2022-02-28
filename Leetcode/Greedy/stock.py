class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        profit = 0
        """ 바로 다음 가격과 비교 후 높으면 +, 낮으면 넘어감 """
        while buy < len(prices)-1 and sell <= len(prices)-1:
            if prices[buy] < prices[sell]:
                p = prices[sell] - prices[buy]
                profit += p
                buy = sell
                sell = buy + 1
            else:
                buy = sell
                sell = buy + 1
        return profit
    
        """ 간단한 솔루션 """
        
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))
