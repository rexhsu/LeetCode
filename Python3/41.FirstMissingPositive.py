class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i] > 0 and nums[i] < n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i, n in enumerate(nums):
            if n != i+1:
                return i+1
        return len(nums)+1
