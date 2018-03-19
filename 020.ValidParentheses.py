class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for c in s:
            if c in left:
                lst.append(c)
            elif c in right:
                if lst and lst.pop() == left[right.index(c)]:
                    continue
                else:
                    return False
        return lst == []
