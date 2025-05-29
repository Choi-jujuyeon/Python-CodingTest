a=input()
stack=[]
count=0
for i in range(len(a)):
    if a[i]=='(':
        stack.append(i)
    elif stack!=[] and a[i]==")":
        stack.pop()
        if a[i-1] == "(":
            count+=len(stack)
        else:
            count+=1
print(count)