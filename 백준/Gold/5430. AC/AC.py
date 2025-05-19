from collections import deque
import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    p=input().strip()
    n=int(input())
    arr=input().strip()
    
    if arr=='[]':
        q=deque()
    else:
        q=deque(map(int,arr[1:-1].split(',')))
    reverse=False
    error = False
    
    for i in p:
        if i=="R":
            reverse=not reverse
        else:
            if not q:
                error=True
                break
            if reverse:
                q.pop()
            else:
                q.popleft()
    if error:
        print("error")
    else:
        if reverse:
            q.reverse()
        print("["+','.join(map(str,q))+"]")