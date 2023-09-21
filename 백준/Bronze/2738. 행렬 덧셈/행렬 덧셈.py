import sys
n,m=map(int,input().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
B=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
C=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        C[i][j]=A[i][j]+B[i][j]
for row in C:
    print(*row)