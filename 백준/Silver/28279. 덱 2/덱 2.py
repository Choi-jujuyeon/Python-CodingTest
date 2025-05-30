from collections import deque
import sys
input=sys.stdin.readline

T=int(input())
q=deque()
for k in range(T):
    a=input().strip()
    if a.startswith('1'):
        _,num=a.split()
        q.appendleft(int(num))

    elif a.startswith('2'):
        _,num=a.split()
        q.append(int(num))
    elif a=='3':
        print(q.popleft() if q else -1)
    elif a=='4':
        print(q.pop() if q else -1)
    elif a=='5':
        print(len(q))
    elif a=='6':
        print(0 if q else 1)
    elif a=='7':
        print(q[0] if q else -1)
    elif a=='8':
        print(q[-1] if q else -1)

