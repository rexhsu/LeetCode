class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roWList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roVList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rInt = 0
        
        i = 0
        j = 0
        while i < len(s) and j < 13:
            target = roWList[j]
            lTarget = len(target)
            if s[i:i+lTarget] == target:
                i = i + lTarget
                rInt += roVList[j]
            else:
                j += 1

        return rInt
