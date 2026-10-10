class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='': return []
        dialMap = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        result = []
        def go(nums, i=0, s=''):
            if len(s)==len(digits):
                result.append(s)
                return
            
            for x in dialMap[nums[i]]:
                go(nums, i+1, s+x)
        
        nums = []
        for x in digits:
            nums.append(int(x))
        print(nums)
        go(nums)
        return result