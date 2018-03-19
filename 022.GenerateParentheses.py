class Solution(object):
    def genLR(self, l, r, rStr, rLst):
        if l > r: return
        if l == 0 and r == 0:
            rLst.append(rStr)
        else:
            if l > 0:
                self.genLR(l-1, r, rStr+'(', rLst)
            if r > 0:
                self.genLR(l, r-1, rStr+')', rLst)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rLst = []
        self.genLR(n, n, "", rLst)
        return rLst
