"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}  # Dictionary to store the value and its index
        for i, num in enumerate(nums):  # Loop through the list with index
            complement = target - num
            if complement in map:
                return [map[complement], i]  # Return the indices of the two numbers
            map[num] = i  # Add the number and its index to the dictionary

# Example usage
x, y = [2, 7, 11, 15], 9
solution = Solution()  # Create an instance of the Solution class
result = solution.twoSum(x, y)  # Call the twoSum method

print(result)  # Output the result
