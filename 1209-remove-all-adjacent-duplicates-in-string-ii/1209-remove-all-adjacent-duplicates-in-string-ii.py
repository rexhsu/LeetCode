class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        siz, stack = len(s), []
        for c in s:
            if not stack or c != stack[-1][0]: 
                stack.append([c, 1])
            else: # c match stack top
                if stack[-1][1] == k-1: # add c will reach k
                    stack.pop()
                else:
                    stack[-1][1] += 1
        
        return ''.join(c * cnt for c, cnt in stack)