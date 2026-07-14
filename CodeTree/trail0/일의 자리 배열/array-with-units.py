a,b=map(int,input().split())
print(a,b,end=" ")
for _ in range(8):
    new = (a+b)%10
    print(new,end=" ")
    a=b
    b=new


