class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        siz = len(graph)
        
        set1 = set()
        set2 = set()
        
        que = collections.deque()
        handle = 0
        
        for i in range(siz):
            if graph[i]:
                handle += 1
                que.append(i)
            
        set1.add(0)
        level = 0
        
        while que:
            for _ in range(handle): # just handle this level
                i = que.popleft()
                handle -= 1

                if i in set1:
                    for n in graph[i]:
                        if n in set1: return False
                        else: set2.add(n)
                elif i in set2:
                     for n in graph[i]:
                        if n in set2: return False
                        else: set1.add(n)
                else:
                    for n in graph[i]:
                        if n in set1: set2.add(i)
                        if n in set2: set1.add(i)
                    if i == level: # this level must put in a group, randomly assign to set1
                        set1.add(i)
                    handle += 1 # leave i to next level
                    que.append(i)
            level += 1
            #print("que", que, "s1 s2", set1, set2, "lv, handle", level, handle)  
        
        return True
            
                
