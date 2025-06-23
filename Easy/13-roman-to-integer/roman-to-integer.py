class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        while i < len(s):
            if (s[i] == 'I' and i+1 < len(s) and s[i+1] in ('V', 'X')) or (s[i] == 'X' and i+1 < len(s) and s[i+1] in ('L', 'C')) or (s[i] == 'C' and i+1 < len(s) and s[i+1] in ('D', 'M')):
                total += values[s[i+1]] - values[s[i]]
                i += 2
                continue
            total += values[s[i]]
            i += 1
        return total