class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        subStr = ""
        for c in s:
            if c in subStr:
                subStr = subStr[subStr.index(c)+1:]+c
            else:
                subStr += c
            if len(subStr) > maxlen:
                maxlen = len(subStr)
        return maxlen
