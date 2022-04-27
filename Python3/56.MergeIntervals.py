class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 0 <= starti <= endi <= 10^4
        siz = len(intervals)
        if siz == 1: return intervals
        
        siv = sorted(intervals, key = lambda s: s[0])
        ans = []
        curL, curR = siv[0] # current interval
        
        for i in range(1, siz):
            #print(siv[i])
            il, ir = siv[i]
            if il <= curR: # overlap, check if need update curR
                curR = max(curR, ir)
            else: # not overlap, create a new interval
                ans.append([curL, curR]) # append previous interval
                curL = il
                curR = ir
            if i == siz -1: # final interval, append record anyway
                ans.append([curL, curR])

        return ans
