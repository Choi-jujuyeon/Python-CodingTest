class Solution:
    def simplifyPath(self, path: str) -> str:
        pp=path.split("/")
        stack=[]

        for i in pp:
            if not i or i ==".":
                continue
            if i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+"/".join(stack)
            

        