h,m=map(int,input().split())
result=h*60+m-45
if result<0:
    result+=24*60
rh=result//60
rm=result%60
print(rh,rm)