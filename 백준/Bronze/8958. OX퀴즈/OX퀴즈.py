T = int(input())
for _ in range(T):
    quiz = input().strip()
    score = 0
    consecutive = 0
    for ch in quiz:
        if ch == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    print(score)
