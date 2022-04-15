import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordLen = len(beginWord)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            currItem = queue.popleft()
            currWord = currItem[0]; currLen = currItem[1]
            for i in xrange(wordLen):
                prefix = currWord[:i]; postfix = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = prefix + j + postfix
                    if nextWord == endWord: return currLen+1
                    if nextWord in wordList:
                        queue.append((nextWord, currLen + 1))
                        wordList.remove(nextWord)
        return 0
