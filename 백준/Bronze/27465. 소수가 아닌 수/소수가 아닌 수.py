a=int(input())
if a==1:
    print(4)
 
else:
    val=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            val=False
    if val:
        print(a*2)
    else:
        print(a)