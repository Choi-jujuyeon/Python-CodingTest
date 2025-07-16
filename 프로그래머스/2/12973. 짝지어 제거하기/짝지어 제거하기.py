def solution(s):
    stack=[]
    for i in s:
        if stack!=[] and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1
            
            