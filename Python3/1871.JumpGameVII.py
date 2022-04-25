class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # 2 <= s.length <= 10^5
        # s[0] = '0'
        # 1 <= minJump <= maxJump < s.length
        # greedy is wrong
        # try dp
        # hint 2: reachable if sum of i-maxJump to i-minJump < number of nodes
        # after watch video, try bfs => TLE for worst cases
        siz = len(s)
        
        if s[-1] == '1': return False
        
        q, farest = collections.deque([0]), 0
        
        while q:
            #print(q)
            idx = q.popleft()
            minJ = max(idx+minJump, farest+1)
            maxJ = min(idx+maxJump, siz-1)
            if minJ > siz -1: break
            for pos in range(minJ, maxJ+1):
                #print("try pos", pos)
                if  pos > farest and s[pos] == "0":
                    if pos == siz-1: return True
                    q.append(pos)
            farest = maxJ
        
        return farest == siz-1
