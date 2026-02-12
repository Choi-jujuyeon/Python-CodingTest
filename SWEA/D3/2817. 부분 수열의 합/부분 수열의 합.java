import java.util.Scanner;

class Solution {

    static int N, K, cnt;
    static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {

            N = sc.nextInt();
            K = sc.nextInt();

            arr = new int[N];
            for (int i = 0; i < N; i++)
                arr[i] = sc.nextInt();

            cnt = 0;

            dfs(0, 0);
            System.out.println("#" + tc + " " + cnt);
        }
    }

    static void dfs(int idx, int sum) {

        if (idx == N) {
            if (sum == K) cnt++;
            return;
        }
        dfs(idx + 1, sum);
        dfs(idx + 1, sum + arr[idx]);
    }
}
