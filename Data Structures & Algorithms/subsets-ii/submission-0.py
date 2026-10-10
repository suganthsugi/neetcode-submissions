class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def go(s=[], ind = 0):
            result.append(s)

            for i in range(ind, len(nums)):
                if i==ind or (nums[i]!=nums[i-1]):
                    go(s+[nums[i]], i+1)
        
        go()
        return result