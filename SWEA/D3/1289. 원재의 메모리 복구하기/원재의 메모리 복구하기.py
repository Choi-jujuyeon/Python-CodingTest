T=int(input())
for k in range(T):
    a=input().strip()
    prev='0'
    count=0
    for i in a:
        if i!=prev:
            count+=1
            prev=i
    print(f'#{k+1} {count}')