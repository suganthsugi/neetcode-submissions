class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        i=0
        for x in tokens:
            if x in ['*', '-', '+', '/']:
                val2 = stk.pop() 
                val1 = stk.pop()
                result = val1+val2
                if x=="-":
                    result = val1-val2
                if x=="*":
                    result = val1*val2
                if x=="/":
                    result = int(val1/val2)
                stk.append(result)
            else:
                stk.append(int(x))
        return int(stk[-1])