def solution(picture, k):
    arr = []
    for row in picture:
        expanded_row = "".join([char * k for char in row])  # 가로 확장
        for _ in range(k):  # 세로 확장
            arr.append(expanded_row)
    return arr
