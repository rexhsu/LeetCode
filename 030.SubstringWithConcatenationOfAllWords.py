class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections
        import json
        dct  = collections.defaultdict(int)
        for w in words:
            dct[w] += 1
        # print json.dumps(dct)
        res, l = [], len(words[0])
        for i in range(l):
            tmp_dct, j = dct.copy(), i
            while j < len(s) - l + 1:
                tmp_dct[s[j:j+l]] -= 1
                while tmp_dct[s[j:j+l]] < 0:
                    tmp_dct[s[i:i+l]] += 1
                    i += l
                j += l
                if (j-i) / l == len(words) :
                    res.append(i)
        return res
