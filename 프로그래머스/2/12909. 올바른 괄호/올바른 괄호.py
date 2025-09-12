def solution(s):
    
    stack=[]
    dic={
        ")":"("
    }
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return False if stack else True
                
            
            
        