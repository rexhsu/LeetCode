class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1: return  "1"
        num = [str(i) for i in range(1, n+1)]
        fac = [1]
        for i in range(1, n-1):
            fac.append((i+1)*fac[i-1])
        sol = []
        k -= 1 # index from 0
        for i in range(n-2, -1, -1):
            #f = math.factorial(i)
            f = fac[i]
            sol.append(num.pop(int(k/f)))
            k = k%f
        sol.append(num.pop())
        #print(num, sol, ''.join(sol))
        return ''.join(sol)