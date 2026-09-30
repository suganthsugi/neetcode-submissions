class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_id = []
        t_id = []
        print(ord('z'))
        for i in range(0, 26):
            s_id.append(i)
            t_id.append(i)
        
        for x in s:
            s_id[ord(x)-ord('a')] += 1
        for x in t:
            t_id[ord(x)-ord('a')] += 1
        
        return s_id==t_id