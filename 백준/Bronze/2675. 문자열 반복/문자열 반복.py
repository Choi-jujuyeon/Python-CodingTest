a=int(input())
for _ in range(a):
    b,c=input().split()
    ib=int(b)
    for j in c:
        print(j*ib,end="")
    print()
    