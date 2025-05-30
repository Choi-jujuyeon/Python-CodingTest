n = int(input())
line = list(map(int, input().split()))
stack = []
order = 1

for student in line:
    while stack and stack[-1] == order:
        stack.pop()
        order += 1

    if student == order:
        order += 1
    else:
        stack.append(student)

# 스택에 남아있는 학생들도 확인
while stack and stack[-1] == order:
    stack.pop()
    order += 1

print("Nice" if not stack else "Sad")
