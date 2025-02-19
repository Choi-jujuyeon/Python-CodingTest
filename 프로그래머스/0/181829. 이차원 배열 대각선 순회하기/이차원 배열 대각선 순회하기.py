def solution(board, k):
    row=len(board)
    col=len(board[0]) 
    return sum(board[i][j] for i in range(row) for j in range(col) if i+j<=k)