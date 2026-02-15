import java.util.Arrays;
import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int N = sc.nextInt();
            int lo = sc.nextInt();
            int hi = sc.nextInt();
            int[] ws = new int[N];
            
            for (int i = 0; i < N; i++) ws[i] = sc.nextInt();
            Arrays.sort(ws);
            
            int result = Integer.MAX_VALUE;
            
            for (int i = lo; i <= N - 2 * lo; i++) {
                int lowCount = i;

                if (lowCount > hi) continue;
                if (ws[i - 1] == ws[i]) continue;

                for (int j = i + lo; j <= N - lo; j++) {
                    int midCount = j - i;
                    int highCount = N - j;

                    if (midCount > hi || highCount > hi) continue;
                    if (ws[j - 1] == ws[j]) continue;

                    int mx = Math.max(lowCount, Math.max(midCount, highCount));
                    int mn = Math.min(lowCount, Math.min(midCount, highCount));
                    result = Math.min(result, mx - mn);
                }
            }

            if (result == Integer.MAX_VALUE) result = -1;
            System.out.println("#" + tc + " " + result);
        }

        sc.close();
    }
}
