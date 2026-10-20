class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_num = nums[i]
            for j in range(i + 1, len(nums)):
                second_num = nums[j]
                if first_num + second_num == target:
                    return [i, j]