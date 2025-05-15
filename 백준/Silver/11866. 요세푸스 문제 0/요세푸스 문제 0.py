from collections import deque

a,b=map(int,input().split())
q=deque(range(1,a+1))
result=[]

while q:
    for _ in range(b-1):
        q.append(q.popleft())
    result.append(q.popleft())
print("<" + ", ".join(map(str,result))+">")