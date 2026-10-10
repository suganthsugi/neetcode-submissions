class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def go(s=[], ind = 0):
            result.append(list(s))

            for i in range(ind, len(nums)):
                if i==ind or (nums[i]!=nums[i-1]):
                    s.append(nums[i])
                    go(s, i+1)
                    s.pop()
        
        go()
        return result