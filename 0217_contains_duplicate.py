"""
LeetCode #217 - Contains Duplicate

Link:
https://leetcode.com/problems/contains-duplicate/

Pattern:
Array + Hash Set

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def containsDuplicate(self, nums):

        # Stores numbers that we have already encountered.
        # Since a set only keeps unique values, it helps us
        # detect whether a number appeared before.
        seen = set()

        for num in nums:

            # If the number already exists in the set,
            # a duplicate value has been found.
            if num in seen:
                return True

            # Store the current number for future checks.
            seen.add(num)

        # If we complete the loop without finding any duplicate,
        # all elements are unique.
        return False


"""
Approach:
Use a Hash Set to keep track of numbers that have already appeared.

For each element:
1. Check whether the number is already present in the set.
2. If it exists, return True because a duplicate is found.
3. Otherwise, add it to the set and continue.

Why this approach?
A brute-force solution compares every pair of elements,
which takes O(n²) time.

A Hash Set provides average O(1) lookup, allowing us to
scan the array only once.

Example:
nums = [1,2,3,1]

1 → store
2 → store
3 → store
1 → already exists → duplicate found

Key Insight:
When a problem asks:
"Have I seen this value before?"

Think:
Hash Set / Hash Map

"""

