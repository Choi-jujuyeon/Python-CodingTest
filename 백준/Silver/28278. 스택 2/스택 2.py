import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for i in range(n):
    cmd=input().strip()
    if cmd.startswith('1'):
        _,num=cmd.split()
        stack.append(int(num))
    elif cmd=='2':
        if stack!=[]:
            print(stack.pop())
            
        else:
            print(-1)
    elif cmd=='3':
        print(len(stack))
    elif cmd=='4':
        if stack==[]:
            print(1)
        else:
            print(0)
    elif cmd=="5":
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])
