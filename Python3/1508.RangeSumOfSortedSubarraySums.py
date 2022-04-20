class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lt = []
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                lt.append(s)
        lt.sort()
        return sum(lt[left-1:right]) % 1000000007
