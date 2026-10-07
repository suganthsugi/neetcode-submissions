class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = math.inf

        for x in nums:
            result = min(result, x)
        
        return result