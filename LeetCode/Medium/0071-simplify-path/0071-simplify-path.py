class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []                       
        parts = path.split("/")          
        for part in parts:                
            if not part or part == ".":   
                continue                  
            if part == "..":             
                if stack:                 
                    stack.pop()          
            else:
                stack.append(part)        
        return "/" + "/".join(stack) 
            