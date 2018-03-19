class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        pth = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in pth:
                lst.append(c)
            else:
                if lst and c == pth[lst.pop()]:
                    continue
                else:
                    return False
        return lst == []
