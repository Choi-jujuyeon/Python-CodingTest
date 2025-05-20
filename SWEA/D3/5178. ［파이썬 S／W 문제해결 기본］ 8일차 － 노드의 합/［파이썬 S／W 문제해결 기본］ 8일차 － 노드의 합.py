T=int(input())
for k in range(T):
    a,b,c=map(int,input().split())
    tree=[0]*(a+1)
    for _ in range(b):
        idx,num=map(int,input().split())
        tree[idx]=num
    # print(tree)
    #부모 노드 구하기
    for i in range(a//2,0,-1):
        total=0
        if i*2<=a:
            total+=tree[i*2]
        if i*2+1<=a:
            total+=tree[i*2+1]
        tree[i]=total
    print(f'#{k+1} {tree[c]}')
    