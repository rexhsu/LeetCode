class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lt = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                lt.append(sum)
        lt.sort()
        ans = 0
        # print(lt)
        for i in range(left-1, right):
            ans += lt[i]
            ans = ans % 1000000007
        return ans
