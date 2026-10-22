class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        num_set = set(nums)
        cont = []
        for num in nums:
            if num - 1 not in num_set: # starting value
                seq_len = 1
                while num + seq_len in num_set:
                    seq_len += 1
                cont.append(seq_len)
        return max(cont)