class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roWList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roVList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rStr = ""
        
        for v in roVList:
            if num >= v:
                c = num / v
                num %= v
                rStr += roWList[roVList.index(v)]*c

        return rStr
