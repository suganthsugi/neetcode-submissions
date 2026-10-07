class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        visited = set([])
        result = 0
        while p1<len(s) and p2<len(s):
            while p2<len(s) and s[p2] not in visited:
                visited.add(s[p2])
                p2+=1
            result = max(result, p2-p1)
            while p2<len(s) and p1<=p2 and s[p2] in visited:
                visited.remove(s[p1])
                p1+=1
        
        return result