a=sorted(list(map(int,input().split())))
if a[2]<a[0]+a[1]:
    print(sum(a))
else:
    a[2]=a[2]-1-abs(a[2]-a[0]-a[1])
    print(sum(a))   