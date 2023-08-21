import sys
for i in range(int(input())):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")