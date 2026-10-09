class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        match = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for x in s:
            if x in ['(', '[', '{']:
                stk.append(x)
            elif len(stk)>0 and stk[-1] == match[x]:
                stk.pop()
            else:
                stk.append(x)
        if stk==[]:
            return True
        return False