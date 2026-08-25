class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        greatest = 0
        max_f = 0
        L = 0

        seen = {}

        #vlaid window = (R - L + 1 ) - chnages <= k
        for R in range(len(s)):

            if s[R] in seen:
                seen[s[R]] += 1
            else:
                seen[s[R]] = 1
            max_f = max(max_f, seen[s[R]])
            while (R - L + 1) - max_f > k:
                seen[s[L]] -= 1
                L += 1
            greatest = max(greatest, sum(seen.values()))

        print(seen)


        return greatest




        