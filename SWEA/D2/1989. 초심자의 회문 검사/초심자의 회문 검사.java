T=int(input())
for t in range(1,T+1):
    a=input()
    l,r=0,len(a)-1
    result=1
    
    while(l<r):
        if a[l]!=a[r]:
            result=0
            break
        l+=1
        r-=1
        
    
    print(f"#{t} {result}")