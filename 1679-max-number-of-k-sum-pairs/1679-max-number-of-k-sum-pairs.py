class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        1 <= nums[i] <= 10^9
        """
        arr = [i for i in nums if i < k]
        print(arr)
        
        arr = sorted(arr)
        
        sol = 0
        i, j = 0, len(arr)-1
        while i<j:
            if arr[i] + arr[j] > k:
                j-=1
            elif arr[i] + arr[j] < k:
                i+=1
            else:
                sol += 1
                i, j = i+1, j-1
                
        return sol
            