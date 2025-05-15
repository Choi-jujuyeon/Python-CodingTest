import sys
from collections import deque

input=sys.stdin.readline
q=deque()
T=int(input())

for _ in range(T):
    cmd=input().strip()
    
    if "push" in cmd:
        _,num = cmd.split()
        q.append(int(num))
    elif "pop" in cmd:
        print(q.popleft() if q else -1)
    elif "size" in cmd:
        print(len(q))
    elif "empty" in cmd:
        print(0 if q else 1)
    elif "front" in cmd:
        print(q[0] if q else -1)
    elif "back" in cmd:
        print(q[-1] if q else -1)   