class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            if r - l + 1 - max(freq.values()) <= k:
                res = max(r - l + 1, res)
            else:
                freq[s[l]] -= 1
                l += 1
        return res