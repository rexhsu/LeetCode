class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lst = [""] * numRows
        unit = 2*(numRows-1)
        numUnit = 0
        for i in range(0, len(s)):
            if unit == 0:
                mod = i
            else:
                mod = i % unit
            if mod < numRows:
                lst[mod] += s[i]
            else:
                lst[unit - mod] += s[i]
        return ''.join(lst)
