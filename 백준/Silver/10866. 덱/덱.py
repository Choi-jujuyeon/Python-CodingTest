from collections import deque
import sys
input=sys.stdin.readline
T=int(input())
q=deque()

for i in range(T):
    cmd=input().strip()
    
    if cmd.startswith("push_back"):
        _,num=cmd.split()
        q.append(int(num)) 
        
    elif cmd.startswith("push_front"):
        _,num=cmd.split()
        q.appendleft(int(num)) 
        
    elif cmd == "pop_front":
        print(q.popleft() if q else -1)
    elif cmd == "pop_back":
        print(q.pop() if q else -1)
    elif cmd == "size":
        print(len(q) if q else 0)
    elif cmd == "empty":
        print(0 if q else 1)
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[-1] if q else -1)