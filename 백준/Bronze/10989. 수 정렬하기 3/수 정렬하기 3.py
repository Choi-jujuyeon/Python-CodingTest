import sys
input = sys.stdin.readline

n = int(input())
MAX = 10001  # 숫자 범위가 1~10000이라면

count = [0] * MAX

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, MAX):
    for _ in range(count[i]):
        print(i)
