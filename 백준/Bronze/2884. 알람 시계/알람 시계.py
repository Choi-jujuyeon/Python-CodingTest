h,m=map(int,input().split())
mm=(h*60+m)-45
H=mm//60
M=mm%60

if mm<0:
    print(23,60+mm)
else:
    print(H,M)