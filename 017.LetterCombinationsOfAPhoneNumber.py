class Solution(object):
    def listCombinations(self, list1, list2):
        rLst = []
        for i in list1:
            for j in list2:
                rLst.append(i+j)
                
        return rLst

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        rLst = []
        bts = { '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], 
                '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], 
                '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        for d in digits:
            """print "d:", d, " bts[d],", bts[d]"""
            if rLst == []:
                rLst = bts[d]
            else:
                rLst = self.listCombinations(rLst, bts[d])
            """print "rLst,", rLst"""
        
        return rLst
