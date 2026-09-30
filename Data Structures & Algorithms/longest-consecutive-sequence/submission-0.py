class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unums = set(nums)
        result = 0
        for x in nums:
            tRes = 1
            if x-1 not in unums:
                while x+1 in unums:
                    tRes+=1
                    x+=1
                result = max(result, tRes)

        return result