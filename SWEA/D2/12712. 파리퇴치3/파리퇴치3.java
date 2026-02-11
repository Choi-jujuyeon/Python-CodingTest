import java.util.Scanner;

class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int tc=1; tc<=T; tc++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[][] arr = new int[N][N];

            for(int i=0; i<N; i++)
                for(int j=0; j<N; j++)
                    arr[i][j] = sc.nextInt();

            int max = 0;

            int[] dr1 = {0, 1, 0, -1};
            int[] dc1 = {1, 0, -1, 0};

            int[] dr2 = {-1, 1, 1, -1};
            int[] dc2 = {1, 1, -1, -1};

            for(int r=0; r<N; r++) {
                for(int c=0; c<N; c++) {

                    int pSum = arr[r][c];
                    for(int d=0; d<4; d++) {
                        for(int k=1; k<M; k++) {
                            int nr = r + dr1[d]*k;
                            int nc = c + dc1[d]*k;
                            if(nr < 0 || nr >= N || nc < 0 || nc >= N) break;
                            pSum += arr[nr][nc];
                        }
                    }

                    int xSum = arr[r][c];
                    for(int d=0; d<4; d++) {
                        for(int k=1; k<M; k++) {
                            int nr = r + dr2[d]*k;
                            int nc = c + dc2[d]*k;
                            if(nr < 0 || nr >= N || nc < 0 || nc >= N) break;
                            xSum += arr[nr][nc];
                        }
                    }

                    int best = Math.max(pSum, xSum);
                    if(max < best) max = best;
                }
            }

            System.out.println("#" + tc + " " + max);
        }
    }
}
