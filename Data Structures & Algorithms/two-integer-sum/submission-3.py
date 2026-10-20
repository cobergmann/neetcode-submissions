class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix, num in enumerate(nums):
            remaining_list = nums[ix+1:]
            if target - num in remaining_list:
                return [
                    ix, remaining_list.index(target-num) + ix + 1
                ]