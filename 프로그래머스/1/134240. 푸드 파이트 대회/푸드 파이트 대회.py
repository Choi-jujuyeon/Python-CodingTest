def solution(food):
    stack=[]
    for idx,num in enumerate(food):
        if idx>0:
            stack.append(str(idx) *(num//2))
    # return stack
    return"".join(stack) + '0' + "".join(stack[::-1])
        
        
        
        
            