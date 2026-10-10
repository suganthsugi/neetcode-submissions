class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def go(ss = [], currSum = 0, ind=0):
            if currSum==target:
                result.append(ss)
            for i in range(ind, len(nums)):
                if currSum+nums[i] <= target:
                    go(ss+[nums[i]], currSum+nums[i], i)
        go()
        return result