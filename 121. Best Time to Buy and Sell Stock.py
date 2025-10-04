'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        buy_date = 0
        profit = 0
        for day, price in enumerate(prices):
            if prices[day] < buy_price:
                buy_price = price
                buy_date = day
            if day == len(prices) - 1:
                return 0
        sell_price = prices[buy_date + 1]
        for sell_date in range(buy_date, len(prices)):
            if prices[sell_date] > sell_price:
                sell_price = prices[sell_date]
        profit = sell_price - buy_price
        return profit

teste = Solution()
print(teste.maxProfit([7,1,5,3,6,4])) #xpected 5
print(teste.maxProfit(prices = [7,1,5,3,6,4]))
print(teste.maxProfit(prices = [7,6,4,3,1]))