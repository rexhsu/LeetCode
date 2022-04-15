class Solution(object):   
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """ Apply Manacher's Algorithm"""
        tranStr = "^"
        for c in s:
            tranStr += "#" + c
        tranStr += "#$"
        """
        print "tranStr: ", tranStr
        """
        
        lenTranStr = len(tranStr)
        lst = [0] * lenTranStr
        center = 0
        right = 0
        
        for i in range(1, len(tranStr)):
            iMirror = 2*center - i
            remain = right - i
            if remain >= 0 and lst[iMirror] < remain:
                    lst[i] = lst[iMirror]
            else:
                if remain >= 0:
                    lst[i] = remain
                else:
                    lst[i] = 0
                while i + lst[i] + 1 < lenTranStr and tranStr[i + lst[i] + 1] == tranStr[i - lst[i] - 1]:
                    lst[i] += 1
                center = i
                right = i + lst[i]
                """
                print "current center:", center, ", right:", right, ",lst", lst
                """
                
        maxlen = max(lst)
        maxidx = lst.index(maxlen)
        maxbegin = (maxidx - 1 - maxlen) / 2

        """
        print "maxlen:", maxlen, ", maxidx:", maxidx, ",maxbegin", maxbegin
        """
        return s[maxbegin : maxbegin + maxlen]

