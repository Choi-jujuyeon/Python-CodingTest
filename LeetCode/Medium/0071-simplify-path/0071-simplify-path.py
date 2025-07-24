class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        cur=""

        for i in path+"/":
            if i=="/":
                if cur=="..":
                    if res:
                        res.pop()
                elif cur!="." and cur!="":
                    res.append(cur)
                cur=""

            else:   #문자열
                cur+=i
        return "/"+"/".join(res)

