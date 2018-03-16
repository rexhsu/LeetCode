class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rStr = str(x)[::-1]
        if rStr[-1] == '-':
            rStr = '-' + rStr[:-1]
        rInt = int(rStr)
        if rInt > pow(2,31) or rInt < -pow(2,31):
            return 0
        else:
            return rInt
