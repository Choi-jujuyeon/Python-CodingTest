T=int(input())
for i in range(T):
    L,U,X=map(int,input().split())
    if X<L:
        result=L-X
    elif L<=X<=U:
        result=0
    else:
        result=-1
    print(f'#{i+1} {result}')