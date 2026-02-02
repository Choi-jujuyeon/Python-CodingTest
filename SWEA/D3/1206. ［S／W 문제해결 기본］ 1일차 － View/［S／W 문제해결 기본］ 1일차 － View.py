import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {
            int T = sc.nextInt();
            int[] arr = new int[T];

            for (int j = 0; j < T; j++) {
                arr[j] = sc.nextInt();
            }

            int result = 0;

            for (int p = 2; p < T - 2; p++) {
                int maxL = Math.max(arr[p - 2], arr[p - 1]);
                int maxR = Math.max(arr[p + 1], arr[p + 2]);
                int M = Math.max(maxL, maxR);

                if (arr[p] > M) {
                    result += (arr[p] - M);
                }
            }

            System.out.printf("#%d %d\n", tc, result);
        }
    }
}
