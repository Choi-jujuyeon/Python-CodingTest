class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        cur ="" #파일 경로 알려줌
        
        for i in path+"/":
            if i =="/":
                if cur=="..":
                    if stack: stack.pop()
                elif cur !="" and cur !=".":
                    stack.append(cur)
                cur=""
            else:
                cur+=i
        return "/"+'/'.join(stack)
