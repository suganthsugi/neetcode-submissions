class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def go(ss=[], ind=0):
            nonlocal result

            result.append(ss)

            for i in range(ind, len(nums)):
                go(ss+[nums[i]], i+1)
        
        go()
        return result