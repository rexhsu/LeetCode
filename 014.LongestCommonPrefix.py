class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        s0 = strs[0]
        diff = 0

        for i in range(0, len(s0)):
            for s in strs[1:]:
                if len(s) <= i or s[i] != s0[i]:
                    diff = 1
                    break
                """print "s0[{0}]:{1} s[{0}]:{2}".format(i, s0[i], s[i])"""
            if diff == 1:
                break
        """print "i:", i"""
        return s0[:i] if diff else s0
