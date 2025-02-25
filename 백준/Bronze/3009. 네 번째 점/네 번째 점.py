from collections import Counter
x,y=[],[]
for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
x2 = [k for k, v in Counter(x).items() if v == 1][0]
y2 = [k for k, v in Counter(y).items() if v == 1][0]

print(x2, y2)