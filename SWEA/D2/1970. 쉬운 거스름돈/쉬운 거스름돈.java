import java.util.Scanner;

class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        int[] money = {50000, 10000, 5000, 1000, 500, 100, 50, 10};

        for (int tc = 1; tc <= T; tc++) {

            int N = sc.nextInt();

            System.out.println("#" + tc);

            for (int coin : money) {
                int count = N / coin; 
                System.out.print(count + " ");
                N %= coin; 
            }

            System.out.println();
        }
    }
}