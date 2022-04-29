class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        siz = len(graph)
        
        grp = [2]*siz # 2 means not group yet, we have only 2 group: 0 & 1

        que = collections.deque()
        handle = 0 # record this level we have to handle
        for i in range(siz):
            if graph[i]:
                handle += 1
                que.append(i)
        grp[0] = 0
        level = 0
        
        while que:
            for _ in range(handle): # just handle this level
                i = que.popleft()
                handle -= 1
                
                if grp[i] != 2:
                    for n in graph[i]:
                        if grp[n] == grp[i]: return False
                        else: grp[n] = (1 - grp[i])
                else:
                    for n in graph[i]:
                        if grp[n] != 2:
                            grp[i] = (1 - grp[n]) # assign to opposite group
                            break
                    if grp[i] == 2 and i == level: # i at this level must enter group, randomly assign to group 0
                        grp[i] = 0
                    handle += 1 # leave i to next level
                    que.append(i)
            level += 1
            print("que", que, "grp", grp, "lv, handle", level, handle)  
        
        return True
            
                
