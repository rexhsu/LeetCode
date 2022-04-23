class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        if goal == 0: return 0
        curReach, maxReach, step = 0, 0, 0
        for i, n in enumerate(nums[:goal]):
            maxReach = max(maxReach, i+n)
            if i == curReach:
                step += 1
                curReach = maxReach
                
        return step
