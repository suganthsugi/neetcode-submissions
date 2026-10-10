class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def go(ss = [], currSum = 0, ind = 0):
            if currSum == target:
                result.append(ss)
            
            for i in range(ind, len(candidates)):
                if currSum+candidates[i] <= target:
                    if i==ind or (candidates[i]!=candidates[i-1]):
                        go(ss+[candidates[i]], currSum+candidates[i], i+1)
        
        go()
        return result