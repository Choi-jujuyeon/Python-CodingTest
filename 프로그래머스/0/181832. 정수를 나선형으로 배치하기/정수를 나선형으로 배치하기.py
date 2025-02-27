def solution(a):

    arr = [[0] * a for _ in range(a)]

    num = 1
    x, y = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    direction = 0

    for _ in range(a * a):
        arr[x][y] = num
        num += 1
        nx, ny = x + dx[direction], y + dy[direction]

        if nx < 0 or nx >= a or ny < 0 or ny >= a or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny

    return arr