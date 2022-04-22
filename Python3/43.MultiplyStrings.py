class Solution:
    def add(self, num1:str, num2: str) -> str:
        if num1 == "": return num2
        if num2 == "": return num1
        rnum1, rnum2 = num1[::-1], num2[::-1]
        l1, l2 = len(num1), len(num2)
        maxlen = max(l1, l2)
        out = ""
        i, a = 0, 0
        while i < maxlen:
            n1, n2 = 0, 0
            if i < l1: n1 = int(rnum1[i])
            if i < l2: n2 = int(rnum2[i])
            i += 1
            s = n1 + n2 + a
            a = s // 10
            out += str(s % 10)
        if a != 0: out += str(a)
        #print("add", num1, num2, out[::-1])
        
        return out[::-1]
        
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        rnum1, rnum2 = num1[::-1], num2[::-1]
        out = "" # global solution
        i = 0
        for c1 in rnum1:
            a = 0
            cur = "" # local solotion
            for c2 in rnum2:
                p = int(c1) * int(c2) + a
                a = p // 10
                cur += str(p % 10)
                #print("cur", cur)
            if a != 0: cur += str(a)
            #print("cur", cur)
            out = self.add(cur[::-1]+"0"*i, out)
            i += 1
            #print(out)
        return out
