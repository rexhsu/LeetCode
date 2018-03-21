class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        r = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[r] = nums[i]
                r += 1
        return r
