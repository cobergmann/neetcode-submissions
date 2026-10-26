class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sorted = sorted(nums)
        i = 0
        curr = nums_sorted[i]
        for i, a in enumerate(nums_sorted):
            if i > 0 and a == nums_sorted[i - 1]:
                continue
            if a > 0:
                break
            l = i + 1
            r = len(nums_sorted) - 1
            while l < r:
                three_sum = a + nums_sorted[l] + nums_sorted[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([
                        a, nums_sorted[l], nums_sorted[r]
                    ])
                    l += 1
                    r -= 1
                    while nums_sorted[l] == nums_sorted[l - 1] and l < r:
                        l += 1

        return res