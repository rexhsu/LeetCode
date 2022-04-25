class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # 1 <= nums.length, k <= 105
        # -104 <= nums[i] <= 104
        # dp: TLE
        # try Hint 2, use MaxHeap
        N = len(nums)
        h = [(-nums[0], 0)] # python heap is a min heap, add negative, store the -score and index
        
        for i in range(1, N):
            #print(h, i-k)
            while h[0][1] < i-k:
                heappop(h)
            cur = h[0][0]
            heappush(h, (cur-nums[i], i))
            if i == N-1:
                return -(cur-nums[i])
        
        return nums[0]
