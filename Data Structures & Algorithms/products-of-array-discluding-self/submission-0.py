class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        p = 1
        zeroCount = 0
        px0 = 1
        for x in nums:
            if x==0:
                zeroCount+=1
            else:
                px0*=x
            p*=x
        
        for x in nums:
            if x==0 and zeroCount==1:
                result.append(px0)
            elif x==0 and zeroCount>1:
                result.append(0)
            else:
                result.append(int(p/x))
        
        return result