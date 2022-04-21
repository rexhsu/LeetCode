class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        def per(nums, s, cur, ans):
            if s == len(nums):
                #print("append", cur)
                #if not cur in ans: ans.append(cur[:])
                ans.append(cur[:])
                return
            p = -11
            for i in range(len(nums)):
                if nums[i] == p: continue
                if used[i]: continue
                used[i] = True
                cur.append(nums[i])
                #print(i, cur)
                per(nums, s+1, cur, ans)
                p = cur.pop()
                used[i] = False
        ans = []
        nums.sort()
        per(nums, 0, [], ans)
        return ans
