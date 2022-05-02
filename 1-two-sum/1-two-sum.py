class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexedNums = [(i, n) for i, n in enumerate(nums)]
        indexedNums = sorted(indexedNums, key=lambda x: x[1])
        #print(indexedNums)
        
        def bsrch(inums, target):
            left, right = 0, len(inums)-1
            while left <= right:
                mid = int((left + right) / 2)
                if target < inums[mid][1]:
                    right = mid - 1
                elif target > inums[mid][1]:
                    left = mid + 1
                else:
                    return inums[mid][0]
            return -1
        
        for i, n in indexedNums:
            j = bsrch(indexedNums, target - n)
            if j != -1 and j != i:
                return [i, j]
            