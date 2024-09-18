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

#print(result)  # Output the result

# Time Complexity : O(n)
# Space Complexity : O(n)

"""

Analysis:

    Queue 1 : What variations can be done on the problem.
    
    
            Parellel Questions:
                1. Print All the pairs which result to target. 
                2. List can have duplicate.


"""

class AlternateSolution:
    def twosumAlternate(self, nums: list[int], target: int):
        index_map = {}  # Dictionary to store number and all its indices
        container = []  # List to store result pairs

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:  # Check if complement exists
                # If complement exists, store all index pairs
                for complement_index in index_map[complement]:
                    container.append((complement_index, i))  # Store the index pair
            # Add the current number's index to the index map (supporting multiple indices for the same number)
            if num in index_map:
                index_map[num].append(i)
            else:
                index_map[num] = [i]

        # Print all the index pairs that sum up to the target
        for index1, index2 in container:
            print(f"Pair: index1={index1}, index2={index2}")

# Time Complexity : O(n)
# Space Complexity : O(n)

# Example usage
x = [2, 2, 7, 7, 11, 15]
y = 9
alternate_solution = AlternateSolution()
alternate_solution.twosumAlternate(x, y)

           