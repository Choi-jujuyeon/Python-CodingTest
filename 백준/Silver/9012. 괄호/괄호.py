import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    k=input().strip()
    stack=[]
    for i in k:
        if stack and (stack[-1]=='(' and i==')'):
            stack.pop()
        elif len(stack)==0 or stack[-1]==i:
            stack.append(i)
    print("NO" if stack else "YES")