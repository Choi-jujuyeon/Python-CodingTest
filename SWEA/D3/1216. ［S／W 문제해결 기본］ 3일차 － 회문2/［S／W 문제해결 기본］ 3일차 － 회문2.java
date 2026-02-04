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
                if (rowPal(arr, row, start, len)) return true;
            }
        }
        return false;
    }

    static boolean colCheck(char[][] arr, int len) {
        for (int col = 0; col < N; col++) {
            for (int start = 0; start <= N - len; start++) {
                if (colPal(arr, col, start, len)) return true;
            }
        }
        return false;
    }

    static boolean rowPal(char[][] arr, int row, int start, int len) {
        int lp = start, rp = start + len - 1;
        while (lp < rp) {
            if (arr[row][lp] != arr[row][rp]) return false;
            lp++; rp--;
        }
        return true;
    }

    static boolean colPal(char[][] arr, int col, int start, int len) {
        int lp = start, rp = start + len - 1;
        while (lp < rp) {
            if (arr[lp][col] != arr[rp][col]) return false;
            lp++; rp--;
        }
        return true;
    }
}
