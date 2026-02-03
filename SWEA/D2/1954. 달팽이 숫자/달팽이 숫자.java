import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int test = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= test; t++) {
            int n = Integer.parseInt(br.readLine().trim());

            int[][] arr = new int[n][n];

            int x = 0;
            int y = 0;
            int dir = 0;

            int[] dx = {1, 0, -1, 0};   // 오른쪽, 아래, 왼쪽, 위
            int[] dy = {0, 1, 0, -1};

            for (int num = 1; num <= n * n; num++) {
                arr[y][x] = num;

                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n || arr[ny][nx] != 0) {
                    dir++;
                    if (dir == 4) dir = 0;
                    nx = x + dx[dir];
                    ny = y + dy[dir];
                }

                x = nx;
                y = ny;
            }

            sb.append("#").append(t).append("\n");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sb.append(arr[i][j]).append(" ");
                }
                sb.append("\n");
            }
        }

        System.out.print(sb.toString());
    }
}
