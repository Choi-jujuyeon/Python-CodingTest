class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0 #섬이 몇개 있는지 체크
        row_len = len(grid)
        col_len = len(grid[0])
        visited=[[False]*col_len for _ in range(row_len)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        
        def dfs(r,c):
            visited[r][c] =True
            for i in range(4):
                next_r = r + dr[i] # 4방향의 다음 좌표
                next_c = c + dc[i]

                if 0<= next_r<row_len and 0<= next_c < col_len:
                    if grid[next_r][next_c] =="1":
                        if not visited[next_r][next_c]:
                            dfs(next_r,next_c)
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] =="1" and not visited[i][j]:
                    dfs(i,j)
                    count+=1
        return count
        