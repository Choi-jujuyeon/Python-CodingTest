T=int(input())

for i in range(T):
    a=input()
    sum = 0
    count=0
    for i in a:
        if i=='X':
            count=0
        else:
            count+=1
            sum+=count
    print(sum)