T=int(input())
for k in range(T):
    path=input().strip()
    a,b=1,1
    for i in path:
        if i=="L":
            b=a+b
        else:
            a=a+b
    print(f'#{k+1} {a} {b}')