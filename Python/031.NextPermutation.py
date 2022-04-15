class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lNums = len(nums)
        i = 0
        for i in range(lNums - 2, -2, -1):
            if nums[i+1] > nums[i]:
                break
        print "i:", i
        if i >= 0:
            for j in range(lNums - 1, -1, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        print "after swap:", nums
        i += 1
        j = lNums - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
