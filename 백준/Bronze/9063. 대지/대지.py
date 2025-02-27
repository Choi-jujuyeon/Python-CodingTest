a=int(input())
xx,yy=[],[]
if a<=1:
    print(0)
else:
    for i in range(a):
        x,y=map(int,input().split())
        xx.append(x)
        yy.append(y)
        
    print((max(xx)-min(xx))*(max(yy)-min(yy)))