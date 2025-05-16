import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
m_arr=list(map(int,input().split()))

counter=Counter(arr)
result = [counter[i] for i in m_arr]

print(*result)