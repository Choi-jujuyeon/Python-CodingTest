h,m=map(int,input().split())
c=int(input())   
tm=(h*60)+m+c
H=tm//60
M=tm%60
if H>=24:
    print(H-24,M)
else:
    print(H,M)
