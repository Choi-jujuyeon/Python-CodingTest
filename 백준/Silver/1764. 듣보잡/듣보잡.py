import sys
input = sys.stdin.readline

n,m=map(int,input().split())
setA=set()
setB=set()
         
for _ in range(n):
    setA.add(input().strip())
for _ in range(m):
    setB.add(input().strip())
setC=setA&setB
print(len(setC))
for i in sorted(setC):
    print(i)