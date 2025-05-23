T=int(input())
for k in range(T):
    a=input()
    count=0
    start='0'
    for i in a:
        if i!=start:
            count+=1
            start=i
    print(f'#{k+1} {count}')
