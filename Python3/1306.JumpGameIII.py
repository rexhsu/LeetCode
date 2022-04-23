class Solution:
    def reach(self, arr, larr, rarr, start) -> bool:
        #print("reach", start)
        #print("larr", larr, "rarr", rarr)
        if arr[start] == 0:
            return True
        left = start - arr[start]
        right = start + arr[start]
        #print("left", left, "right", right)
        if left >= 0 and not larr[start]:
            larr[start] = True
            if self.reach(arr, larr, rarr, left):
                return True
        if right < len(arr) and not rarr[start]:
            rarr[start] = True
            if self.reach(arr, larr, rarr, right):
                return True
        return False
            
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        larr = [False]*l
        rarr = [False]*l
        return self.reach(arr, larr, rarr, start)
        
