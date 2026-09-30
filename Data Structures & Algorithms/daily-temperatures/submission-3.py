class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ind = []
        mds = []
        result = [0]*len(temp)

        for i in range(len(temp)-1, -1, -1):
    
            while len(mds)>0 and mds[-1]<=temp[i]:
                mds.pop()
                ind.pop()
            mds.append(temp[i])
            ind.append(i)
            
            if len(mds) <= 1:
                # print('in here, setting 0')
                result[i] = 0
            else:
                # print('in here,', mds, ind)
                result[i] = ind[-2] - i
            # print(result)
            
        return result