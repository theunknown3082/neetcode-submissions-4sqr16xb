class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            maxf = max(maxf, seen[s[r]])

            while (r - l + 1) - maxf > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res