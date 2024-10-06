https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

----------------------------------------------------------------------------------------------

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

----------------------------------------------------------------------------------------------

Approach:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1
        return maxProfit

Complexity Analysis

-> Time complexity: O(n)

-> Space complexity: O(1)

----------------------------------------------------------------------------------------------
