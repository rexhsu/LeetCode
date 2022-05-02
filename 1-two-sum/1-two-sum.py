class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remains = [(target - i) for i in nums]
        #print(remains)
 
        for i, r in enumerate(remains):
            for j, n in enumerate(nums):
                if i!=j and r==n: return [i, j]