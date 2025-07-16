def solution(k, score):
    stack,res=[],[]
    for i in score:
        if stack==[] or len(stack)<k:
            stack.append(i)         
        else:
            if stack[-1]<i:
                stack.pop()
                stack.append(i)
        stack.sort(reverse=True)
        res.append(stack[-1])
    return res
            
                
                
    