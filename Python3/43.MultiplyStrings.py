class Solution:
    def add(self, num1:str, num2: str) -> str:
        if num1 == "": return num2
        if num2 == "": return num1
        i = len(num1) - 1
        j = len(num2) - 1
        out = ""
        a = 0
        while i >= 0 or j >= 0:
            n1 = 0
            n2 = 0
            if i >= 0:
                n1 = int(num1[i])
                i -= 1
            if j >= 0:
                n2 = int(num2[j])
                j -= 1
            s = n1 + n2 + a
            a = s // 10
            out += str(s % 10)
        if a != 0: out += str(a)
        print("add", num1, num2, out[::-1])
        return out[::-1]
        
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        i = len(num1) - 1
        out = ""
        while i >= 0:
            a = 0
            cur = ""
            j = len(num2) - 1
            while j >= 0:
                n1, n2 = int(num1[i]), int(num2[j])
                p = n1 * n2 + a
                #print(n1, n2, p)
                a = p // 10
                cur += str(p % 10)
                j -= 1
                #print("cur", cur)
            if a != 0: cur += str(a)
            print("cur", cur)
            out = self.add(cur[::-1]+"0"*(len(num1)-1-i), out)
            print(out)
            i -= 1
        return out
