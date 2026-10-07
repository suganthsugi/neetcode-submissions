class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = math.inf

        result = -1
        for x in prices:
            currMin = min(currMin, x)
            result = max(result, x-currMin)
        
        return result