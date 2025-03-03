from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        while True:
            sum_ = nums[l][0] + nums[r][0]
            if sum_ == target:
                return [nums[l][1], nums[r][1]]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        