class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = self.countAndSay(n-1) + '*' # end of string
        out = ""
        key = ''
        cnt = 1
        #print(n, s)
        for c in s:
            if key == '': # first character
                key = c
                cnt = 1
            elif c == key:
                cnt += 1
            else: # c != key || c == '*'
                out = out + str(cnt) + key
                key = c
                cnt = 1
        #print(n, out)
        return out
