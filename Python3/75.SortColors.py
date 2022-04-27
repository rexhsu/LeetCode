class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero put on left side(i)
        # 2 put on right side(k)
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[j] == 0: # swap j to i, i++, next j because j(from i) is visited value
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            elif nums[j] == 1: # next j
                j+=1
            else: # swap j and k, k--, don't next j because j(from k) is not visited
                nums[j], nums[k] = nums[k], nums[j]
                k-=1
