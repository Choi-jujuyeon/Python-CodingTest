import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int t = 1; t <= 10; t++) {
            int T = sc.nextInt();

            int[][] arr = new int[100][100];

            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int max = 0;

            for (int i = 0; i < 100; i++) {
                int sumRow = 0;
                for (int j = 0; j < 100; j++) {
                    sumRow += arr[i][j];
                }
                if (sumRow > max) max = sumRow;
            }

            for (int j = 0; j < 100; j++) {
                int sumCol = 0;
                for (int i = 0; i < 100; i++) {
                    sumCol += arr[i][j];
                }
                if (sumCol > max) max = sumCol;
            }

            int sumLd = 0;
            int sumRd = 0;
            for (int i = 0; i < 100; i++) {
                sumLd += arr[i][i];
                sumRd += arr[i][99 - i];
            }

            if (sumLd > max) max = sumLd;
            if (sumRd > max) max = sumRd;

            System.out.println("#" + T + " " + max);
        }
    }
}
