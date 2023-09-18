import sys
a=int(input())
s=[]
for i in range(a):
    w=sys.stdin.readline().rstrip()
    s.append(w[0]+w[-1])
print(*s)