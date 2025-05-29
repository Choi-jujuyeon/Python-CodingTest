import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정 (필수는 아님, 큰 입력 대비)
input = sys.stdin.readline  # 함수로 저장 (괄호 ❌)

# n: 세로, m: 가로, k: 음식물 수
n, m, k = map(int, input().split())

# 그래프 및 방문 배열 초기화
graph = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[False] * (m + 1) for _ in range(n + 1)]

# 음식물 위치 표시
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

# 상하좌우 이동 좌표
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# DFS 함수 정의
def dfs(x, y):
    size = 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                size += dfs(nx, ny)
    return size

# 최대 음식물 덩어리 크기 찾기
max_size = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, dfs(i, j))

print(max_size)
