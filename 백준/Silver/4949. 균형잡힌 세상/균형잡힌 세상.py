import sys

for line in sys.stdin:
    line = line.rstrip()
    if line == ".":
        break

    stack = []
    balanced = True

    for ch in line:
        if ch in "([":  # 여는 괄호면 스택에 push
            stack.append(ch)
        elif ch == ")":
            if stack and stack[-1] == "(":  # 맞는 짝이 있으면 pop
                stack.pop()
            else:
                balanced = False  # 없거나 짝이 안 맞으면 실패
                break
        elif ch == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break

    # 모두 돌고 나서 스택이 비어 있어야 균형 잡힘
    if balanced and not stack:
        print("yes")
    else:
        print("no")
