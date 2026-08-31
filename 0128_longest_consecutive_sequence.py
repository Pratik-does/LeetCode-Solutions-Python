"""
LeetCode #128 - Longest Consecutive Sequence

Link:
https://leetcode.com/problems/longest-consecutive-sequence/

Pattern:
Hash Set + Sequence Start Detection

Time Complexity:
O(n) average

Space Complexity:
O(n)
"""


class Solution:

    def longestConsecutive(self, nums):

        # Store every number in a Hash Set.
        # This gives average O(1) membership checks.
        lookup = set()

        for num in nums:
            lookup.add(num)

        # Length of the current consecutive sequence.
        current_length = 0

        # Length of the longest consecutive sequence found so far.
        longest = 0

        # Examine each unique number.
        for value in lookup:

            # If value - 1 exists, then value is not the
            # beginning of a consecutive sequence.
            if value - 1 in lookup:
                continue

            # value is the beginning of a new sequence.
            current_length = 0
            num = value

            # Count consecutive numbers starting from value.
            while num in lookup:
                current_length += 1
                num += 1

            # Update the longest sequence found so far.
            if current_length > longest:
                longest = current_length

        return longest


"""
Approach:

1. Put all numbers into a Hash Set.

2. For every number, check whether its predecessor
   (value - 1) exists.

3. If the predecessor exists, skip the number because
   it is already inside an existing consecutive sequence.

4. If the predecessor does not exist, the number is the
   beginning of a sequence.

5. Starting from that number, keep checking:
       value
       value + 1
       value + 2
       ...

   until the next consecutive number is missing.

6. Track the longest sequence found.

Example:

nums = [100, 4, 200, 1, 3, 2]

Sequence starts:
    100 → length 1
    200 → length 1
    1   → 1, 2, 3, 4 → length 4

Numbers such as 2, 3, and 4 are skipped as starting points
because their predecessors already exist.

Key Insight:

A number can start a consecutive sequence only when
(number - 1) is absent from the set.

This prevents repeatedly scanning the same sequence and
allows the overall algorithm to run in O(n) average time.
"""
