from collections import deque
T=int(input())

for i in range(T):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    q=deque([(idx,n) for idx,n in enumerate(arr)])
    
    count=0
    while q:
        cur=q.popleft()
        if any(cur[1]<qq[1] for qq in q):
            q.append(cur)
        else:
            count+=1
            if cur[0]==m:
                print(count)
                break
                