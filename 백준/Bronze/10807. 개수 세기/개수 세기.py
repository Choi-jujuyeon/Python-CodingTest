import sys
from collections import Counter

a = int(input())
b = list(map(int,input().split()))
c = int(input())

print(Counter(b)[c])

