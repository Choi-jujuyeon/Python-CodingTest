def solution(board, moves):
    r,c= len(board), len(board[0])
    stack=[[] for _ in range(c)]
    # print(stack)
    for i in range(c):
        for j in range(r-1,-1,-1):
            if board[j][i]!=0:
                stack[i].append(board[j][i])           
    # print(stack)
    res=[]
    count=0

    for i in moves:
        idx=i-1
        if stack[idx]:
            doll = stack[idx].pop()
            if res and res[-1] == doll:
                res.pop()
                count+=2
            else:
                res.append(doll)
        
    return count
            
    