class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, s, curr, ans):
            print("dfs", target, s, curr, "ans", ans)
            if target == 0:
                ans.append(curr[:])
                return
            for i in range(s, len(candidates)):
                print(i, candidates[i], target)
                if candidates[i] > target: return
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i, curr, ans)
                curr.pop()
        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)
            
        return ans        
