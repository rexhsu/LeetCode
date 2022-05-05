class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1: return  "1"
        num = [str(i) for i in range(1, n+1)]
        sol = []
        k -= 1 # index from 0
        for i in range(n-1, 0, -1):
            f = math.factorial(i)
            idx = int(k/math.factorial(i))
            #print("k i f idx", k, i, f, idx)
            sol.append(num.pop(idx))
            k = k%f
        sol.append(num.pop())
        #print(num, sol, ''.join(sol))
        return ''.join(sol)