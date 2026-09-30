class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for j, x in enumerate(nums):
            target = x
            visited = set([])
            for i in range(j+1, len(nums)):
                if (-target-nums[i]) in visited and sorted([target, -target-nums[i], nums[i]]) not in result:
                    result.append(sorted([target, -target-nums[i], nums[i]]))
                else:
                    visited.add(nums[i])
        return result