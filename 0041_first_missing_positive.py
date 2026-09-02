"""
LeetCode #41 — First Missing Positive

Problem:
Given an unsorted integer array, find the smallest positive integer
that is not present in the array.

Example:
Input:  [3, 4, -1, 1]
Output: 2

Approach:
The main idea is to use the input array itself to keep track of
which positive numbers are present.

For an array of length n, we only care about numbers from 1 to n.
Any number <= 0 or greater than n cannot be the answer directly,
so we replace those values with n + 1.

Then we use the array indexes to represent the numbers:

1 -> index 0
2 -> index 1
3 -> index 2
...

When a number exists, we make the value at its corresponding index
negative. The negative sign acts as a marker that tells us:
"This number is present."

We use abs() because a value may already be negative from an
earlier marking.

After marking, we scan the array from left to right.
The first positive value means that its corresponding number
was never found.

If every position is negative, then all numbers from 1 to n exist,
so the answer is n + 1.

Step-by-step:
1. Replace all useless values with n + 1.
2. Use each valid number to find its corresponding index.
3. Mark that index as negative.
4. Find the first index that is still positive.
5. Return index + 1.

Time Complexity: O(n)

We make three passes through the array, and each pass takes O(n).

Space Complexity: O(1)

We modify the input array itself and do not use any extra data
structure that grows with the input.

Pattern: Clean -> Mark -> Scan
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        upperbound = len(nums) + 1
        length = len(nums)

        # Replace numbers that cannot help us.
        for i, num in enumerate(nums):
            if num <= 0 or num > length:
                nums[i] = upperbound

        # Mark the numbers that are present.
        for i in range(length):
            num = abs(nums[i])

            if 1 <= num <= length:
                value = num - 1
                nums[value] = -abs(nums[value])

        # Find the first number that was not marked.
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        # If all numbers from 1 to n are present,
        # the answer is n + 1.
        return upperbound
