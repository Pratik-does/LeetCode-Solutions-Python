"""
LeetCode #238 - Product of Array Except Self

Link:
https://leetcode.com/problems/product-of-array-except-self/

Pattern:
Array + Prefix Product + Suffix Product

Time Complexity:
O(n)

Space Complexity:
O(1) extra space
"""


class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)

        # answer[i] will first store the product of all
        # elements to the left of index i.
        answer = [1] * n

        # Running product of elements to the left
        # of the current index.
        prefix = 1

        # Traverse from left to right.
        for i in range(n):

            # At this point, prefix contains only the elements
            # before i, so nums[i] is naturally excluded.
            answer[i] = prefix

            # Include nums[i] for the next index.
            prefix *= nums[i]

        # Running product of elements to the right
        # of the current index.
        suffix = 1

        # Traverse from right to left.
        for i in range(n - 1, -1, -1):

            # answer[i] already contains the left product.
            # Multiply it by the product of elements to the right.
            answer[i] *= suffix

            # Include nums[i] for the next index to the left.
            suffix *= nums[i]

        return answer


"""
Approach:
For every index i, the required value is:

    product of elements before i
    ×
    product of elements after i

A brute-force solution recalculates these products for every
index and takes O(n²) time.

Instead, use two passes.

1. Left → Right:
   Store the prefix product in answer[i].

2. Right → Left:
   Maintain a suffix product and multiply it into answer[i].

The current element is never included in either product because
the answer is updated before the current value is added to the
running prefix or suffix.

Example:
nums = [1,2,3,4]

After the prefix pass:
answer = [1,1,2,6]

After the suffix pass:
answer = [24,12,8,6]

Why this approach?
It avoids division, works correctly with zeros, runs in O(n) time,
and uses the output array itself instead of separate prefix/suffix
arrays, giving O(1) extra space.

Key Insight:
When an answer depends on everything before and after an index,
look for a Prefix + Suffix approach.
"""
