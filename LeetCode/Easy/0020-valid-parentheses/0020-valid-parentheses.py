class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            ']':'[',
            ')':'(',
            "}":"{"
        }
        res=[]
        for i in s:
            if i in "{([":
                res.append(i)
            else:
                if not res or dic[i] != res[-1]:
                    return False
                else:
                    res.pop()
        return False if res else True
