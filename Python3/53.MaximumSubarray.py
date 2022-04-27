class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cur, res = nums[0], nums[0]
        curL, curR, resL, resR = 0, 0, 0, 0
        for idx, num in enumerate(nums[1:]):
            if cur < 0: # i-1 contribute nothing, start from i
                cur = num
                #curL, curR = idx+1, idx+1
            else: # i-1 contributes, include i
                cur += num
                #curR = idx+1
            if cur > res:
                res = cur
                #resL, resR = curL, curR
            
        #print(resL, resR)
        return res
