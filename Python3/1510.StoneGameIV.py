class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0]*(n+1)
        for i in range (1, n+1):
            for j in range (1, n+1):
                if j*j > i: break
                if dp[i-j*j] != 1:
                    dp[i] = 1
        #print(dp)
        return dp[n]
