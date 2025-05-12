import math
T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=math.sqrt((x1-x2)**2+ (y1-y2)**2)
    #같은 원
    if r1==r2 and x1==x2 and y1==y2:
        print(-1)
    #한점에서 만날 경우
    elif r1+r2==d or d==abs(r1-r2):
        print(1)
    #아예 안 만날 경우
    elif r1+r2<d or d<abs(r1-r2):
        print(0)

    #두 점에서 만날 경우
    else:
        print(2)
    