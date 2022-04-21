class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            k = ''.join(sorted(item))
            if k not in res:
                res[k] = []
            res[k].append(item)
            print(res)
            
        return [res[x] for x in res]  
