a=int(input())
i=2
while a//i!=0:
    if a%i==0:
        a//=i
        print(i)
    else:
        i+=1