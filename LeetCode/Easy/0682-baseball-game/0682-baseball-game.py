class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if not stack:
                stack.append(int(i))
            else:
                if i=="D":
                    stack.append(stack[-1]*2)
                elif i=="C":
                    stack.pop()
                elif i=="+":
                    stack.append(stack[-1] + stack[-2])
                else:
                    stack.append(int(i))
        return sum(stack)
                    
            

                
        