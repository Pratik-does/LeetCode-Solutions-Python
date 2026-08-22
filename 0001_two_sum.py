"""
LeetCode #1 - Two Sum

Link:
https://leetcode.com/problems/two-sum/

Pattern:
Array + Hash Map

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def twoSum(self, nums, target):

        # Stores previously seen numbers:
        # number -> index
        seen = {}

        for index, num in enumerate(nums):

            # Find the number needed to reach target
            complement = target - num

            # If complement was already seen,
            # we found the required pair
            if complement in seen:
                return [seen[complement], index]

            # Store current number for future lookup
            seen[num] = index

        return []


"""
Approach:
A brute-force approach checks every possible pair,
which takes O(n²) time.

Instead, use a Hash Map to store numbers already visited.
For each number, calculate its complement:

complement = target - current_number

If the complement exists in the map, the answer is found.
Otherwise, store the current number and continue.

Example:
nums = [2,7,11,15], target = 9

2 needs 7.
Store 2.
When 7 appears, its complement already exists.

Key Insight:
Whenever a problem asks for a matching pair,
think about storing previously seen values for O(1) lookup.
"""
