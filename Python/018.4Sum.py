class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, rLst = sorted(nums), []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        k, l = j + 1, len(nums) - 1
                        """print "nums[i]:%d  nums[j]:%d nums[k]:%d nums:%d" % (nums[i], nums[j], nums[k], nums[l])"""
                        while k < l:
                            s = nums[i] + nums[j] + nums[k] + nums[l]
                            if s < target:
                                k += 1
                            elif s > target:
                                l -= 1
                            else:
                                rLst.append([nums[i], nums[j], nums[k], nums[l]])
                                k, l = k + 1, l - 1
                                while k < l and nums[k] == nums[k - 1]:
                                    k += 1
                                while k < l and nums[l] == nums[l + 1]:
                                    l -= 1
        return rLst
