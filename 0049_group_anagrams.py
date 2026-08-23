"""
LeetCode #49 - Group Anagrams

Link:
https://leetcode.com/problems/group-anagrams/

Pattern:
String + Hash Map + Frequency Counting

Time Complexity:
O(n * k)

Space Complexity:
O(n * k)
"""


class Solution:
    def groupAnagrams(self, strs):

        # Maps each frequency signature to the list of
        # strings having that exact character frequency.
        groups = {}

        for word in strs:

            # 26 positions for lowercase English letters.
            # Index 0 -> a, 1 -> b, ..., 25 -> z.
            count = [0] * 26

            # Build the frequency signature for the current word.
            for char in word:
                count[ord(char) - ord("a")] += 1

            # Lists are not hashable, so convert the frequency
            # array into a tuple that can be used as a dictionary key.
            key = tuple(count)

            # Create a new group if this signature has not appeared.
            if key not in groups:
                groups[key] = []

            # Add the word to the group represented by its signature.
            groups[key].append(word)

        return list(groups.values())


"""
Approach:
Anagrams contain exactly the same characters with the same
frequencies, regardless of their order.

For each string, create a 26-element frequency vector.

Example:
    "eat" -> [1,0,0,0,1,0,...,1,...]
    "tea" -> [1,0,0,0,1,0,...,1,...]

Because their frequency vectors are identical, both strings
produce the same key and are placed in the same group.

The frequency vector is used directly as the Hash Map key.

Why this approach?
Sorting every string would cost O(k log k) per string.

Frequency counting takes O(k) per string and uses the fixed
26-character alphabet to build the signature directly.

Example:
strs = ["eat","tea","tan","ate","nat","bat"]

Signatures:
    eat -> same key as tea and ate
    tan -> same key as nat
    bat -> unique key

Result:
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]

Key Insight:
When objects belong to the same group because they share the
same character frequencies, build that frequency signature
and use it as a Hash Map key.
"""
