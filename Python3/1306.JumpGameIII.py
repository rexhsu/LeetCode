class Solution:
    def reach(self, arr, larr, rarr, start) -> bool:
        #print("reach", start)
        #print("larr", larr, "rarr", rarr)
        if arr[start] == 0:
            return True
        left = start - arr[start]
        right = start + arr[start]
        #print("left", left, "right", right)
        if left >= 0 and larr[start] == 0:
            larr[start] = 1
            if self.reach(arr, larr, rarr, left):
                return True
        if right < len(arr) and rarr[start] == 0:
            rarr[start] = 1
            if self.reach(arr, larr, rarr, right):
                return True
        return False
            
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        larr = [0]*l
        rarr = [0]*l
        return self.reach(arr, larr, rarr, start)
