T=int(input())
for k in range(T):
    a,b=map(int,input().split())
    if a<b:
        r='<'
    elif a>b:
        r='>'
    elif a==b:
        r='='
    print(f'#{k+1} {r}')