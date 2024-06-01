"""
121_best_time_to_buy_and_sell_stock.py
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    lowest = prices[0]
    profit = 0

    for price in prices:
        if price - lowest > profit:
            profit = price - lowest
        if price < lowest:
            lowest = price

    return profit


if __name__ == "__main__":
    # Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    result = max_profit([7, 1, 5, 3, 6, 4])
    assert result == 5, result

    result = max_profit([1,2,3,4,5])
    assert result == 4, result

    result = max_profit([7,6,4,3,1])
    assert result == 0, result
