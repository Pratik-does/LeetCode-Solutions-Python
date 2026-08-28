"""
LeetCode #13 - Roman to Integer

Link:
https://leetcode.com/problems/roman-to-integer/

Pattern:
Hash Map + String Traversal

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def romanToInt(self, s):

        # Store the value of every Roman numeral symbol
        # and the six valid subtractive combinations.
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        # Running total of the converted Roman numeral.
        total = 0

        # Current position in the string.
        # We use a manually controlled index because we may
        # consume either one symbol or two symbols at a time.
        i = 0

        # Continue until every character has been processed.
        while i < len(s):

            # Check whether a next character exists.
            if i + 1 < len(s):

                # Build the current two-character combination.
                two_symbols = s[i] + s[i + 1]

                # If it is a valid subtractive combination,
                # process both symbols together.
                if two_symbols in values:
                    total += values[two_symbols]

                    # Both characters have been consumed.
                    i += 2

                else:
                    # The pair is not a valid Roman numeral,
                    # so process only the current symbol.
                    total += values[s[i]]

                    # Move to the next character.
                    i += 1

            else:
                # The last symbol has no character after it,
                # so process it by itself.
                total += values[s[i]]

                # Move beyond the final character.
                i += 1

        return total


"""
Approach:
Scan the Roman numeral from left to right.

At each position:
1. Check whether the current and next symbols form one of
   the six valid subtractive combinations:
       IV, IX, XL, XC, CD, CM

2. If they do, add the pair's value and move forward by 2.

3. Otherwise, add the current symbol's value and move forward by 1.

4. If the current symbol is the final character, process it alone.

Example:
s = "MCMXCIV"

M   -> 1000
CM  -> 900
XC  -> 90
IV  -> 4

Total = 1994

Why this approach?
The input is guaranteed to be a valid Roman numeral, so checking
the six valid subtractive pairs is sufficient. A manually controlled
index lets the algorithm consume either one or two characters without
needing separate loops.

Key Insight:
At every position, decide whether to consume one symbol or a valid
two-symbol subtractive pair.
"""
