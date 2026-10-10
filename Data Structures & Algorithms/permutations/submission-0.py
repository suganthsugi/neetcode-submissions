class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def go(s=[], visited = set([])):
            if len(s) == len(nums):
                result.append(list(s))
            
            for i in range(len(nums)):
                if i not in visited:
                    s.append(nums[i])
                    visited.add(i)
                    go(s, visited)
                    s.pop()
                    visited.remove(i)
        
        go()
        return result