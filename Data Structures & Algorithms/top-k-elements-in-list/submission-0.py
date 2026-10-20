class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_count = defaultdict(int)

        for num in nums:
            int_count[num] += 1

        return [key for key, value in sorted(int_count.items(), key=lambda x: x[1], reverse=True)[:k]]