a=int(input())
arr=[int(input()) for _ in range(a)]

stack=[]
result=[]
current=1

for num in arr:
    while current<=num:
        stack.append(current)
        result.append('+')
        current+=1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    for i in result:
        print(i)
        