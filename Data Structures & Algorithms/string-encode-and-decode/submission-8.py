class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for x in strs:
            s+=f'{len(x)}-{x}'
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        
        result = []
        i=0
        while i<len(s):
            count = ''
            while s[i]!='-':
                count+=s[i]
                i+=1
            count = int(count)
            currStr = ''
            for j in range(i+1, i+1+count):
                currStr+=s[j]
            result.append(currStr)
            i+=count+1
        return result
                