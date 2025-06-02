N = int(input())
F = int(input())

N -= N % 100  # 뒤 두 자리를 00으로 만든다

for i in range(100):
    if (N + i) % F == 0:
        print(f"{i:02d}")  # 두 자리수로 출력 (앞에 0 붙임)
        break
