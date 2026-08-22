"""
LeetCode #219 - Contains Duplicate II

Link:
https://leetcode.com/problems/contains-duplicate-ii/

Pattern:
Array + Hash Map

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):

        # Stores the most recent index where each number appeared.
        # number -> latest index
        last_seen = {}

        for index, num in enumerate(nums):

            # If the number appeared before,
            # check whether the distance between the two indices
            # is within the allowed range k.
            if num in last_seen and index - last_seen[num] <= k:
                return True

            # Update the latest position of the current number.
            # If it appeared before, we keep only the newest index
            # because it gives the smallest possible distance.
            last_seen[num] = index

        # No duplicate values were found within distance k.
        return False


"""
Approach:
Use a Hash Map to store the latest index of every number.

For each element:
1. Check if the number has appeared before.
2. Calculate the distance between the current index and
   its previous occurrence:

       distance = current_index - previous_index

3. If the distance is <= k, a nearby duplicate exists.
4. Update the number's index to the current position.

Why this approach?
A brute-force approach checks every possible pair of indices,
which takes O(n²) time.

The Hash Map allows us to find previous occurrences in
average O(1) time, reducing the solution to O(n).

Example:
nums = [1,2,3,1], k = 3

1 appears at index 0.
When we reach index 3:

distance = 3 - 0 = 3

Since 3 <= k, return True.

Key Insight:
When a problem asks:
"Have I seen this value before, and how far away was it?"

Think:
Hash Map storing value + index
"""
