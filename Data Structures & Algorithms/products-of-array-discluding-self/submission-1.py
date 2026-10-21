class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, total_prod = [], 1
        for num in nums:
            total_prod *= num
        
        for ix, num in enumerate(nums):
            if num != 0:
                res.append(total_prod // num)
            else:
                curr_prod = 1
                temp_nums = nums[:ix] + nums[ix+1:]
                for num in temp_nums:
                    curr_prod *= num

                res.append(curr_prod)
        return res