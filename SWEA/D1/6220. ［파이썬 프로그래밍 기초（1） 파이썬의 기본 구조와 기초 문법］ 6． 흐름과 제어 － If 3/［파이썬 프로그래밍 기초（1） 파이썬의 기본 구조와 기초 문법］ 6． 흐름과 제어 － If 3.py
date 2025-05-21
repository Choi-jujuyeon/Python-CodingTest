T = int(input())
for i in range(1, T + 1):
    ch = input()
    if 'a' <= ch <= 'z':
        print(f'#{i} {ch} 는 소문자 입니다.')
    else:
        print(f'#{i} {ch} 는 대문자 입니다.')