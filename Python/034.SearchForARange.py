class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = nums.index(target) if target in nums else -1
        j = i
        while j >= 0 and j < len(nums):
            if nums[j] != target:
                j -= 1
                break
            j += 1
        if j == len(nums):
            j -= 1
        return [i, j]
