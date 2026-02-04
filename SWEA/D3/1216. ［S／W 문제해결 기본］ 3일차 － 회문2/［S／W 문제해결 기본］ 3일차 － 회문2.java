import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

    static final int N = 100;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc <= 10; tc++) {
            int testNum = Integer.parseInt(br.readLine().trim());

            char[][] arr = new char[N][N];

            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                for (int j = 0; j < N; j++) {
                    arr[i][j] = line.charAt(j);
                }
            }

            int result = findResult(arr);
            System.out.println("#" + testNum + " " + result);
        }
    }

    static int findResult(char[][] arr) {
        for (int len = N; len >= 1; len--) {
            if (rowCheck(arr, len)) return len;
            if (colCheck(arr, len)) return len;
        }
        return 1;
    }

    static boolean rowCheck(char[][] arr, int len) {
        for (int row = 0; row < N; row++) {
            for (int start = 0; start <= N - len; start++) {
                if (RowPalindrome(arr, row, start, len))
                    return true;
            }
        }
        return false;
    }

    static boolean colCheck(char[][] arr, int len) {
        for (int col = 0; col < N; col++) {
            for (int start = 0; start <= N - len; start++) {
                if (ColPalindrome(arr, col, start, len))
                    return true;
            }
        }
        return false;
    }

    static boolean RowPalindrome(char[][] arr, int row, int start, int len) {
        StringBuilder sb = new StringBuilder(len);

        for (int j = start; j < start + len; j++) {
            sb.append(arr[row][j]);
        }

        String origin = sb.toString();
        String reversed = sb.reverse().toString();

        return origin.equals(reversed);
    }

    static boolean ColPalindrome(char[][] arr, int col, int start, int len) {
        StringBuilder sb = new StringBuilder(len);

        for (int i = start; i < start + len; i++) {
            sb.append(arr[i][col]);
        }

        String origin = sb.toString();
        String reversed = sb.reverse().toString();

        return origin.equals(reversed);
    }
}
