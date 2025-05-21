T=int(input())
for k in range(T):
    a = input()
    y = a[:4]
    m = a[4:6]
    d = a[6:]
    s=False
    if int(m)==2 and 1<=int(d)<=28:
        s=True
    elif int(m) in [1,3,5,7,8,10,12] and 1<=int(d)<=31:
        s=True
    elif int(m) in [4,6,9,11] and 1<=int(d)<=30:
        s=True

    if s:
        print(f'#{k+1} {y}/{m}/{d}')
    else:
        print(f'#{k+1} -1')