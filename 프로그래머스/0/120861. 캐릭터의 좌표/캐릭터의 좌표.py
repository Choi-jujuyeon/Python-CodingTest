def solution(keyinput, board):
    group={
        'up':[0,1],
        'down': [0,-1],
        'right':[1,0],
        'left':[-1,0]
    }

    x,y=0,0
    for i in keyinput:
        x+=group[i][0]
        y+=group[i][1]
        
        if abs(x)>abs(board[0]//2):
            if x>0:
                x=board[0]//2
            else:
                x=board[0]//2*(-1)
                
        if abs(y)>abs(board[1]//2):
            if y>0:
                y=board[1]//2
            else:
                y=board[1]//2*(-1)
    return([x,y])
            