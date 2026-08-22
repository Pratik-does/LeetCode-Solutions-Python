"""
LeetCode #242 - Valid Anagram

Link:
https://leetcode.com/problems/valid-anagram/

Pattern:
String + Frequency Counting

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def isAnagram(self, s, t):

        # An anagram must contain the same number of characters.
        # Different lengths mean the character frequencies cannot match.
        if len(s) != len(t):
            return False

        # Frequency array for lowercase English letters.
        #
        # Index mapping:
        # a -> 0
        # b -> 1
        # c -> 2
        # ...
        # z -> 25
        count = [0] * 26

        # Add characters from s and remove characters from t.
        # If both strings contain the same character frequencies,
        # all values will balance back to zero.
        for char_s, char_t in zip(s, t):

            # Convert character into array index and update frequency.
            count[ord(char_s) - ord("a")] += 1
            count[ord(char_t) - ord("a")] -= 1

        # Any non-zero value means a character frequency mismatch.
        for frequency in count:
            if frequency != 0:
                return False

        return True


"""
Approach:
Instead of sorting both strings and comparing them,
we count character frequencies.

For every character:
- Increase the frequency from string s.
- Decrease the frequency from string t.

If s and t are anagrams, every character appears the same
number of times, so the final frequency array contains only zeros.

Example:
s = "anagram"
t = "nagaram"

After balancing:
a = 0
n = 0
g = 0
r = 0
m = 0

No unmatched characters remain, so return True.


Why this approach?
Sorting:
    Time: O(n log n)

Frequency Counting:
    Time: O(n)

Since the input contains only lowercase English letters,
a fixed-size array of 26 elements provides O(1) extra space.

Key Insight:
When a problem asks whether two strings contain the same
characters with the same frequency, think:

Frequency Counter → Hash Map / Counting Array
"""
