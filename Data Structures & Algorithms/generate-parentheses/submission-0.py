class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def go(s='(', o=1, c=0, lastChar = '('):
            if o==n and c==n:
                result.append(s)
            
            if lastChar=='(':
                if o<n:
                    go(s+'(', o+1, c, '(')
                if c<n:
                    go(s+')', o, c+1, ')')
            if lastChar==')':
                if o<n:
                    go(s+'(', o+1, c, '(')
                if c<=o-1 and c<n:
                    go(s+')', o, c+1, ')')
        
        go()
        return result