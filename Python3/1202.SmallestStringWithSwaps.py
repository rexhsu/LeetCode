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
            
        for p in pairs:
            rx, ry = find(p[0]), find(p[1])
            if rx != ry: roots[ry] = rx
                
        for c in range(siz): groups[find(c)].append(c) # gather indexes with same root
        
        arr = [0]*siz # for modify to be new string
        
        for g in groups:
            chs = [s[i] for i in groups[g]] # pick all characters in groups[g]
            chs.sort() # alphabet sorting for same root
            for i, p in enumerate(groups[g]):
                arr[p] = chs[i]
        
        return ''.join(arr)
            
