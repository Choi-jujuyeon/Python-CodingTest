class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={
            "}":"{",
            ")":"(",
            "]":"["
        }
        for i in s:
            if i in "{([":
                stack.append(i)
            else:
                if stack and stack[-1] == closeToOpen[i] :
                    stack.pop()
                else: return False
        return False if stack else True
