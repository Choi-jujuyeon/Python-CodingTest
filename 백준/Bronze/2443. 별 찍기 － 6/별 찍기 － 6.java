import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++) {

            // 공백
            for (int j = 1; j <= i - 1; j++) {
                System.out.print(" ");
            }

            // 별
            for (int j = 1; j <= 2 * (N - i) + 1; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
