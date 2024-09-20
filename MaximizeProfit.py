"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
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
 

 0 7 1 5 3 6 4
 7 0 0 0 0 0 0   
 1     4 2 5 4
 5         1   
 3
 6
 4
"""

class Solution:
  def maxProfit(prices: list[int]) -> int:
    # Edge case: if there are no prices or only one price, no transaction is possible
    if not prices or len(prices) == 1:
        return 0

    min_price_so_far = float('inf')  # Initialize with a large number
    max_profit = 0  # Maximum profit is 0 initially

    # Traverse through the list of prices
    for price in prices:
        # Update the minimum price so far
        if price < min_price_so_far:
            min_price_so_far = price
        
        # Calculate potential profit for selling at the current price
        potential_profit = price - min_price_so_far
        
        # Update the maximum profit if this is the highest so far
        if potential_profit > max_profit:
            max_profit = potential_profit
    
    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5 (Buy at 1, sell at 6)

# Time Complexity : O(n)