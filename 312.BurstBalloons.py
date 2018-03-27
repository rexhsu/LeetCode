class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        w = len(nums)
        matrix = [[-1 for x in range(w)] for y in range(w)]
        return self.getCoins(1, w-2, matrix, nums)
        
    def getCoins(self, beg, end, matrix, nums):
        if beg > end: return 0
        if matrix[beg][end] != -1: return matrix[beg][end]
    
        for i in range(beg, end + 1):
            leftCoin = self.getCoins(beg, i-1, matrix, nums)
            midCoin = nums[beg-1]*nums[i]*nums[end+1]
            rightCoin = self.getCoins(i+1, end, matrix, nums)
            coin = leftCoin + midCoin + rightCoin
            if coin > matrix[beg][end]:
                matrix[beg][end] = coin
        return matrix[beg][end]
