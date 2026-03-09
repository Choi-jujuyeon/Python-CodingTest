import java.util.*;

class Solution {
    static int count;
    static Set<Integer> cols;
    static Set<Integer> diag1;
    static Set<Integer> diag2;

    static void backtrack(int row, int n) {
        if (row == n) {
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.contains(col) || diag1.contains(row - col) || diag2.contains(row + col)) {
                continue;
            }

            cols.add(col);
            diag1.add(row - col);
            diag2.add(row + col);

            backtrack(row + 1, n);

            cols.remove(col);
            diag1.remove(row - col);
            diag2.remove(row + col);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int n = sc.nextInt();

            count = 0;
            cols = new HashSet<>();
            diag1 = new HashSet<>();
            diag2 = new HashSet<>();

            backtrack(0, n);

            System.out.println("#" + tc + " " + count);
        }
    }
}