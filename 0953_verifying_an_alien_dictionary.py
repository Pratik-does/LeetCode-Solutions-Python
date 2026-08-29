"""
LeetCode #953 - Verifying an Alien Dictionary

Link:
https://leetcode.com/problems/verifying-an-alien-dictionary/

Pattern:
Hash Map + Two-Pointer String Comparison

Time Complexity:
O(n * m)

Space Complexity:
O(1)

Where:
n = number of words
m = maximum length of a word
"""


class Solution:
    def isAlienSorted(self, words, order):

        # Map each alien character to its position in the
        # alien alphabet so characters can be compared by rank.
        store = {}

        for position, character in enumerate(order):
            store[character] = position

        # Compare every pair of adjacent words.
        # If every adjacent pair is correctly ordered,
        # the complete list is sorted.
        i = 0

        while i + 1 < len(words):

            # Start comparing the current pair from
            # the first character.
            character = 0

            # Only positions that exist in both words
            # can be compared.
            limit = min(len(words[i]), len(words[i + 1]))

            while character < limit:

                current = words[i][character]
                next_character = words[i + 1][character]

                # The first different character determines
                # the ordering of the two words.
                if current != next_character:

                    # Current character comes later in the
                    # alien alphabet, so the words are invalid.
                    if store[current] > store[next_character]:
                        return False

                    # Current character comes earlier, so this
                    # pair is correctly ordered. No more
                    # characters from this pair need checking.
                    break

                # Characters are equal, so continue to the
                # next character.
                character += 1

            else:
                # The inner loop finished without a break,
                # meaning all characters of the shorter word
                # matched. In that case, the shorter word must
                # come first.
                if len(words[i]) > len(words[i + 1]):
                    return False

            # Move to the next adjacent pair.
            i += 1

        # Every adjacent pair passed the ordering rules.
        return True


"""
Approach:

1. Build a ranking map from the alien alphabet.

       character -> alien position

   Example:
       h -> 0
       l -> 1
       a -> 2

2. Compare adjacent words only.

       words[0] vs words[1]
       words[1] vs words[2]
       ...

3. Compare each pair character by character.

4. At the first different character:
       - smaller alien position -> pair is valid
       - larger alien position  -> return False

5. If all characters match, apply the prefix rule:
       the shorter word must come first.

Example:

    words = ["word", "world"]

At the first difference:

    d vs l

If the alien order gives:

    d -> 4
    l -> 3

then d comes after l, so the list is not sorted.

Key Insight:

The first different character decides the order.
If no different character exists, word length decides it.
"""
