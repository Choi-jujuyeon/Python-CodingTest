h,m,s=map(int,input().split())
t=int(input())

h+=t//3600
t%=3600
m+=t//60
t%=60
s+=t

if s>=60:
    m+=s//60
    s%=60
if m>=60:
    h+=m//60
    m%=60
h%=24
print(h,m,s)