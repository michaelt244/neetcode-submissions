class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        greatest = 0
        L = 0

        seen = {}

        #vlaid window = (R - L + 1 ) - chnages <= k
        for R in range(len(s)):
            if s[R] in seen:
                seen[s[R]] += 1
            else:
                seen[s[R]] = 1
            if (R - L + 1) - max(seen.values()) > k:
                seen[s[L]] -= 1
                L += 1
            greatest = max(greatest, sum(seen.values()))

        print(seen)


        return greatest




        