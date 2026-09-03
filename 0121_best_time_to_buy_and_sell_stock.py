"""
LeetCode #121 — Best Time to Buy and Sell Stock

Problem:
Given an array of stock prices, buy the stock once and sell it later.
The goal is to get the maximum possible profit.

Example:
prices = [7, 1, 5, 3, 6, 4]
Answer = 5

Approach:
The main idea is to keep track of the cheapest price we have seen so far.

For every price, we ask:
"If I sell today, how much profit can I make?"

Profit is:
current price - buying price

If we find a cheaper price, we update the buying price.

If we find a bigger profit, we update the maximum profit.

We only move from left to right, so the buying price will always
come before the selling price.

Step-by-step:
1. Start with the first price as the buying price.
2. Start the profit at 0.
3. Check each price one by one.
4. If the current price is cheaper, update the buying price.
5. Calculate the profit using current price - buying price.
6. Keep the maximum profit.
7. Return the maximum profit.

Example walkthrough:
prices = [7, 1, 5, 3, 6, 4]

Start:
buy = 7
profit = 0

7 -> no better buying price, profit = 0
1 -> cheaper, so buy = 1
5 -> profit = 5 - 1 = 4
3 -> profit = 3 - 1 = 2, so profit stays 4
6 -> profit = 6 - 1 = 5
4 -> profit = 4 - 1 = 3, so profit stays 5

Final answer:
5

Time Complexity:
O(n)

We go through the prices only once.

Space Complexity:
O(1)

We only use a few variables, so the extra space does not grow
with the size of the input.

Pattern:
Find minimum -> calculate profit -> keep maximum
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]

        for num in prices:
            if num < buy:
                buy = num

            current_profit = num - buy

            if current_profit > profit:
                profit = current_profit

        return profit
