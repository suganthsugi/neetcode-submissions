class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {}

        for i, x in enumerate(nums):
            req = target - x
            if req in visitedMap:
                return [visitedMap[req], i]
            else:
                visitedMap[x] = i