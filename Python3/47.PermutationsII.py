class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        def p(nums, s, cur, ans):
            if s == len(nums):
                print("append", cur)
                if not cur in ans:
                    ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                cur.append(nums[i])
                print(i, cur)
                p(nums, s+1, cur, ans)
                cur.pop()
                used[i] = False
        ans = []
        cur = []
        p(nums, 0, [], ans)
        return ans
