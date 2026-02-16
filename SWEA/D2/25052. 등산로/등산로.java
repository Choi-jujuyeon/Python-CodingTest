import java.util.Scanner;

class Solution {

    static int N;
    static int[][] arr;
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            N = sc.nextInt();
            arr = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int maxLen = 0;

            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int len = getLen(r, c);
                    if (len > maxLen) maxLen = len;
                }
            }

            System.out.println("#" + tc + " " + maxLen);
        }
    }

    static int getLen(int r, int c) {
        int cur = arr[r][c];

        int nextR = -1;
        int nextC = -1;
        int min = Integer.MAX_VALUE;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

            if (arr[nr][nc] < cur && arr[nr][nc] < min) {
                min = arr[nr][nc];
                nextR = nr;
                nextC = nc;
            }
        }

        if (nextR == -1) return 1;

        return 1 + getLen(nextR, nextC);
    }
}
