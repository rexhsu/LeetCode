class Solution:
    res = None
    def uniquePaths(self, m: int, n: int) -> int:
        # path steps down(m-1) + right(n-1)
        # method (m-1)!*(n-1)!
        #print("m n", m, n)
        if m == 1 or n == 1: return 1 # uni-direction
        if self.res == None:
            self.res = [[0]*(n+1) for _ in range(m+1)]
        if self.res[m-1][n] == 0:
            self.res[m-1][n] = self.uniquePaths(m-1, n)
        if self.res[m][n-1] == 0:
            self.res[m][n-1] = self.uniquePaths(m, n-1)
        
        return self.res[m-1][n] + self.res[m][n-1]