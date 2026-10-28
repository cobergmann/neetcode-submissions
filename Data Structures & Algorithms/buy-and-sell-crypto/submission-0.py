class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        i = 0
        diffs = [0]
        while i < len(prices) - 1:
            max_diff = max(prices[i+1:]) - prices[i]
            if max_diff > 0: diffs.append(max_diff)
            i += 1

        return max(diffs)