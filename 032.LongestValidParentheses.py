class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = [-1]
        rInt = 0
        for i in range(len(s)):
            if s[i] == '(':
                lst.append(i)
            else:
                lst.pop()
                if (lst == []):
                    lst.append(i)
                else:
                    rInt = max(rInt, i - lst[-1]) 
        return rInt
