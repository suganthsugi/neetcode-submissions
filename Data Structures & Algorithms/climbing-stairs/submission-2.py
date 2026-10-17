class Solution:
    def climbStairs(self, n: int) -> int:
        result = []
        if n == 1 or n==2:
            return n
        
        s1, s2 = 1, 2
        for i in range(n-2):
            s1, s2 = s2, s1+s2
        # print(s1, s2)
        return s2