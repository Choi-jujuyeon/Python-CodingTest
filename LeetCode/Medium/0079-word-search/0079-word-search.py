class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board의 행(row)과 열(column)의 개수를 구함
        n, m = len(board), len(board[0])

        # 방문 여부를 저장할 2차원 리스트를 False로 초기화
        visited = [[False for _ in range(m)] for _ in range(n)]

        # 단어를 찾았는지 여부를 저장 (True면 탐색 종료)
        answer = False

        #-----------------------------
        # 현재 좌표 (i, j)가 board 범위 안에 있는지 확인하는 함수
        #-----------------------------
        def in_range(i, j):
            return 0 <= i < n and 0 <= j < m

        #-----------------------------
        # 핵심: 백트래킹 (재귀적으로 단어를 찾는 함수)
        # i, j: 현재 탐색 중인 칸의 좌표
        # w: 현재 단어에서 찾고 있는 글자의 인덱스
        # visited: 방문한 칸을 표시하기 위한 리스트
        #-----------------------------
        def backtracking(i, j, w, visited):
            # 현재 칸이 방문 전이고, 글자가 word[w]와 같을 때만 탐색 진행
            if not visited[i][j] and board[i][j] == word[w]:
                # 만약 w가 단어의 마지막 글자라면 → 전부 찾은 것이므로 True 반환
                if w == len(word) - 1:
                    return True

                # 방문했다고 표시
                visited[i][j] = True
                flag = False  # 단어를 찾았는지 임시로 저장할 변수

                # 상, 하, 좌, 우 방향으로 이동 (총 4방향)
                for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    # 이동할 좌표가 범위 안에 있을 때만
                    if in_range(i + x, j + y):
                        # 다음 글자(w+1)를 찾아서 재귀 호출
                        if backtracking(i + x, j + y, w + 1, visited):
                            flag = True  # 단어를 찾았으면 flag를 True로 설정
                            break  # 이미 찾았으니 더 탐색할 필요 없음

                # 다른 경로에서도 탐색할 수 있도록 방문 표시 해제
                visited[i][j] = False

                # 현재 경로에서 단어를 찾았는지 결과 반환
                return flag

            # 글자가 다르거나 이미 방문했다면 False 반환
            return False

        #-----------------------------
        # board 전체를 돌면서 단어 탐색 시작
        # (모든 칸을 단어의 시작점으로 시도)
        #-----------------------------
        for i in range(n):
            for j in range(m):
                if backtracking(i, j, 0, visited):
                    return True  # 단어를 찾으면 True 즉시 반환

        # 모든 칸에서 찾아봤는데도 없으면 False
        return False
