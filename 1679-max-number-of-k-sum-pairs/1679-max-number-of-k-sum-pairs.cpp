class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        1 <= nums[i] <= 10^9
        """
        arr = [i for i in nums if i < k] # filter larger than k. O(n)
        arr = sorted(arr) # O(nlogn)
        #print(arr)
        
        sol, i, j = 0, 0, len(arr)-1
        while i<j: # O(n)
            if arr[i] + arr[j] > k:
                j-=1
            elif arr[i] + arr[j] < k:
                i+=1
            else:
                sol, i, j = sol+1, i+1, j-1
                
        return sol
            