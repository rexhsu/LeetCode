class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        cts, ctd = None, None
        
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while (left < right):
                    ts = nums[i] + nums[left] + nums[right]
                    td = ts - target
                    """print "i:%d left:%d right:%d ts:%d td:%d" % (i, left, right, ts, td)"""
                    if cts == None:
                        cts, ctd = ts, td
                    elif abs(td) < abs(ctd):
                        cts, ctd = ts, td
                    if td < 0:
                        left += 1
                    elif td > 0:
                        right -= 1
                    else:
                        return target

        return cts
