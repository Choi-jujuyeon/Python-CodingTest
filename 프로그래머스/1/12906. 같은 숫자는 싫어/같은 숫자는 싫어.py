def solution(arr):
    stack=[arr[0]]
    # stack=[]
    
    for i in arr:
        if stack[-1] ==i:
            continue
        else:
            stack.append(i)
        # if stack:
        #     if stack[-1] !=i:
        #         stack.append(i)
        #     else:
        #         continue
        # else: stack.append(i)
            
    return stack
                