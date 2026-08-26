"""
LeetCode #347 - Top K Frequent Elements

Link:
https://leetcode.com/problems/top-k-frequent-elements/

Pattern:
Hash Map + Bucket Sort

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def topKFrequent(self, nums, k):

        # Store each number and how many times it appears.
        # number -> frequency
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Bucket index represents frequency.
        #
        # bucket[1] -> numbers appearing once
        # bucket[2] -> numbers appearing twice
        # ...
        # bucket[n] -> numbers appearing n times
        #
        # n + 1 buckets are needed because frequency can be n.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Place each number into the bucket matching its frequency.
        for num, count in frequency.items():
            buckets[count].append(num)

        # Traverse frequencies from highest to lowest.
        # The first k elements encountered are the k most frequent.
        result = []

        for count in range(len(nums), 0, -1):

            for num in buckets[count]:
                result.append(num)

                # Stop as soon as we have k elements.
                if len(result) == k:
                    return result


"""
Approach:
First, count the frequency of every number using a Hash Map.

Example:
nums = [1,1,1,2,2,3]

Frequency:
    1 -> 3
    2 -> 2
    3 -> 1

A sorting-based solution could order the numbers by frequency,
but that would take O(n log n) time.

Instead, use the frequency itself as a bucket index.

For example:
    frequency 1 -> bucket[1]
    frequency 2 -> bucket[2]
    frequency 3 -> bucket[3]

After placing every number into its frequency bucket,
scan the buckets from highest frequency to lowest and collect
elements until k elements have been found.

Why this approach?
The maximum possible frequency is n, so frequencies already
have a bounded range from 1 to n. This lets us avoid sorting
and achieve O(n) time.

Example:
nums = [1,1,1,2,2,3], k = 2

Buckets:
    bucket[3] -> [1]
    bucket[2] -> [2]
    bucket[1] -> [3]

Scan from highest frequency:
    take 1
    take 2

Result:
    [1, 2]

Key Insight:
For "Top K Frequent" problems, first build a frequency map.
If the frequency range is bounded, use the frequency as a
bucket index instead of sorting.
"""
