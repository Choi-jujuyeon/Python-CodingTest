class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack=[]
        for i in s:
            if i in dic:
                if stack and dic[i] == stack[-1]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True

