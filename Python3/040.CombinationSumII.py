class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, s, curr, ans):
            print("dfs", target, s, curr, "ans", ans)
            if target == 0:
                if not curr in ans:
                    ans.append(curr[:])
                return
            p = -1
            for i in range(s, len(candidates)):
                if candidates[i] == p:
                    continue
                print(i, candidates[i], target)
                if candidates[i] > target: return
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i+1, curr, ans)
                p = curr.pop()
        ans = []
        candidates.sort()
        print("candidates after sort", candidates)
        dfs(candidates, target, 0, [], ans)
            
        return ans  
