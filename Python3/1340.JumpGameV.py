class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # dfs? dp? # both of them
        dp = [0]*1000

        def maxJumpsFrom(arr, d, i) -> int:
            if dp[i] != 0: return dp[i]
            ans = 1
            for x in range(1, d+1):
                if i-x < 0: break
                if arr[i-x] >= arr[i]: break
                ans = max(ans, maxJumpsFrom(arr, d, i-x) + 1)
            for x in range(1, d+1):
                if i+x >= len(arr): break
                if arr[i+x] >= arr[i]: break
                ans = max(ans, maxJumpsFrom(arr, d, i+x) + 1)
            dp[i] = ans
            return ans

        for i in range(len(arr)):
            if dp[i] == 0: maxJumpsFrom(arr, d, i)

        return max(dp) 
