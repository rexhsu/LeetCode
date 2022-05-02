class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = [(target - i) for i in nums]
        print(remains)
 
        for i, r in enumerate(remains):
            for j, n in enumerate(nums):
                if i!=j and r==n: return [i, j]
            