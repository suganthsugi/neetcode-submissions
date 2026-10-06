class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = max(piles)
        result = maxP
        left, right = 1, maxP

        while left<=right:
            k = math.floor((right-left)/2)+left

            currRes = 0
            for x in piles:
                currRes+=math.ceil(x/k)

            if(currRes<=h):
                right = k-1
                result = min(result, k)
            else:
                left = k+1
            print(currRes, h, left, right, k)
        
        return result