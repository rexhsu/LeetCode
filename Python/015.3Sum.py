class Solution(object):
    def threeSum(self, nums):
        nums, result = sorted(nums), []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left, right = i + 1, len(nums) - 1
                while (left < right):
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        left, right =  left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result
