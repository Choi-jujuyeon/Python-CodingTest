class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            ']':'[',
            ')':'(',
            '}':'{',
        }
        stack=[]
        for i in s:
            if i in ']})':
                if stack==[] or stack[-1]!= dic[i] :
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return False if stack else True