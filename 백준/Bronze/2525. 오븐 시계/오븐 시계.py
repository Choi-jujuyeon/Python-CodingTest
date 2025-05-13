sh,sm=map(int,input().split())
t=int(input())
result=sh*60+sm+t
h=result//60
m=result%60
if h>=24: h%=24
print(h,m)