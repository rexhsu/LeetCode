class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cur, res = nums[0], nums[0]
        for num in nums[1:]:
            if cur < 0: # i-1 contribute nothing: case1
                cur = num
            else:
                cur += num # case2
            res = max(res, cur) 
            # if res update because case1, l=r=current index
            # if res update because case2, r=current index
            
        return res
