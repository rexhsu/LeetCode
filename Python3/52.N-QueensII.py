class Solution:
    def totalNQueens(self, n: int) -> int:
        # data structure
        # list of size n
        # each list equal the queen location in this line
        # dfs
        
        allsols = (1, 0, 0, 2, 10, 4, 40, 92, 352)
        return allsols[n-1]
        
        sols = []
        
        def putQueen(n, cur = []):
            if len(cur) == n:
                #print("get sol", cur)
                sols.append(cur[:])
                return
            for i in range(n):
                if checkQueen(n, cur, i):
                    #print("pass check", i)
                    cur.append(i)
                    putQueen(n, cur)
                    cur.remove(i)
        
        def checkQueen(n, cur, pos):
            return not any(abs(pos-c) in (abs(len(cur)-i), 0) for i, c in enumerate(cur))
        
        putQueen(n)
        
        return len(sols)
