import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {

            sc.nextInt();

            int[][] a = new int[100][100];

            int x = 0;
            int y = 0;

            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    a[i][j] = sc.nextInt();
                    if (a[i][j] == 2) {
                        y = i;
                        x = j;
                    }
                }
            }

            while (y > 0) {

                if (x > 0 && a[y][x - 1] == 1) {
                    x = x - 1;
                    while (x > 0 && a[y][x - 1] == 1) {
                        x = x - 1;
                    }
                    y = y - 1;
                } else if (x < 99 && a[y][x + 1] == 1) {
                    x = x + 1;
                    while (x < 99 && a[y][x + 1] == 1) {
                        x = x + 1;
                    }
                    y = y - 1;
                } else {
                    y = y - 1;
                }
            }

            System.out.println("#" + tc + " " + x);
        }
    }
}
