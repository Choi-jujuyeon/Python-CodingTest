while True:
    x,y,z=map(int,input().split())
    if x==0 and y==0 and z==0:
        break
    
    a=sorted([x,y,z])
    s=len(set(a))
    if a[2]>=a[0]+a[1]:
        print("Invalid")
        
    elif s==1:
        print("Equilateral")
    elif s==2:
        print("Isosceles")    
    else:
        print("Scalene")