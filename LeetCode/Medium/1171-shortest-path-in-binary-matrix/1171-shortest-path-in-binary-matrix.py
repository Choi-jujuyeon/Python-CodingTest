class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def bfs(grid):
            result=-1
            rows, cols = len(grid), len(grid[0])

            # 출발지, 도착지가 벽이라면 바로 -1 반환
            if grid[0][0] == 1 or grid[rows-1][cols-1] ==1:
                return result
            
            visited = [[False]*cols for _ in range(rows)]
            directions=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

            q = deque()
            q.append((0,0,1))
            visited[0][0] = True

            while q:
                cur_r, cur_c, cur_dist = q.popleft()
                
                if cur_r==rows-1 and cur_c==cols-1:
                    result = cur_dist
                    break
                
                for dr, dc in directions:
                    next_r=dr+cur_r
                    next_c=dc+cur_c

                    if next_r in range(rows) and next_c in range(cols) and grid[next_r][next_c]==0 and not visited[next_r][next_c]:
                        q.append((next_r,next_c,cur_dist+1))
                        visited[next_r][next_c] = True
            return result
        return bfs(grid)