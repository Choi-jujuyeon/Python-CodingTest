from itertools import combinations
from collections import deque, Counter
import sys

input = sys.stdin.readline
rows,cols = map(int,input().split())
board=[list(map(int,input().split())) for _ in range(rows)]

virus, zero=[],[]
answer=0

for r in range(rows):
    for c in range(cols):
        if board[r][c] ==0:
            zero.append([r,c])
        elif board[r][c] ==2:
            virus.append([r,c])

def bfs():
    global answer
    tmp = [board[i][:] for i in range(rows)]
    queue = deque(virus)
    
    while queue:
        r,c=queue.popleft()
        
        for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            next_r,next_c = dr+r, dc+c
            
            if next_r in range(rows) and next_c in range(cols):
                if tmp[next_r][next_c]==0:
                    tmp[next_r][next_c] = 2
                    queue.append((next_r,next_c))
    
    count = Counter()
    for r in tmp:
        count+=Counter(r)
    
    answer=max(answer,count[0])
    return

for new_wall in combinations(zero,3):
    row,col=[],[]
    
    for r,c in new_wall:
        row.append(r)
        col.append(c)
        
        if board[r][c] != 0:
            break
        
    else:
        for i in range(3):
            board[row[i]][col[i]] = 1
        bfs()
        for i in range(3):
            board[row[i]][col[i]] = 0

print(answer)

        