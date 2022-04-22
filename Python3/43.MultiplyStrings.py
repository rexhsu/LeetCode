class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]: return "0"
        
        l1, l2 = len(num1), len(num2)
        res = [0]*(l1 + l2)
        rnum1, rnum2 = num1[::-1], num2[::-1]
        
        for i1 in range(l1):
            for i2 in range(l2):
                digit = int(rnum1[i1]) * int(rnum2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10
                #print(i1, i2, res)
        
        res, beg = res[::-1], 0
        # count the leading zero length
        while beg < len(res) and res[beg] == 0:
            beg += 1
        #print("res before map", res)
        res = map(str, res[beg:])
        
        return "".join(res)
