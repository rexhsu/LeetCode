class Solution:
    def minJumps(self, arr: List[int]) -> int:
        siz = len(arr)
        if siz == 1:
            return 0
        validx = defaultdict(list)
        for i, num in enumerate(arr):
            validx[num].append(i)
        
        queue = collections.deque([0])
        seen = set()
        seen.add(0)
        level = 0
        
        while queue != []:
            for _ in range(len(queue)):
                idx = queue.popleft()
                cur = []
                if idx > 0:
                    cur.append(idx-1)
                if idx+1 < siz:
                    cur.append(idx+1)
                if arr[idx] in validx:
                    cur.extend(validx[arr[idx]])
                    del validx[arr[idx]]
                for e in cur:
                    if e not in seen:
                        if e == siz - 1:
                            return level + 1
                        seen.add(e)
                        queue.append(e)
            level += 1
            
        return level
