class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        siz = len(s)
        if siz == 1: return s
        groups = collections.defaultdict(list)
        roots = [-1]*siz
        
        def find(x):
            if roots[x] == -1: return x
            else: 
                roots[x] = find(roots[x])
                return roots[x]
        
        def union(x, y):
            #print("union", x, y)
            rx, ry = find(x), find(y)
            if rx != ry: roots[ry] = rx
        
        for p in pairs: union(p[0], p[1])

        for c in range(siz): groups[find(c)].append(c)
        #print("groups", groups)
        
        arr = list(s)
        
        for g in groups:
            chs = [s[i] for i in groups[g]]
            chs.sort()
            for i, p in enumerate(groups[g]):
                arr[p] = chs[i]
        
        return ''.join(arr)
