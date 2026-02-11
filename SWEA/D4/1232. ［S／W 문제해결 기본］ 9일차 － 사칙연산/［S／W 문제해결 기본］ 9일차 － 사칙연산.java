import java.util.Scanner;

class Solution {

    static int N;
    static double[] val;
    static char[] op;
    static int[] left, right;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int tc = 1; tc <= 10; tc++) {

            N = sc.nextInt();

            val = new double[N + 1];
            op = new char[N + 1];
            left = new int[N + 1];
            right = new int[N + 1];

            for (int i = 0; i < N; i++) {

                int idx = sc.nextInt();
                String s = sc.next();

                if (s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")) {
                    op[idx] = s.charAt(0);
                    left[idx] = sc.nextInt();
                    right[idx] = sc.nextInt();
                } else {
                    val[idx] = Double.parseDouble(s);
                }
            }

            double result = calc(1);

            System.out.println("#" + tc + " " + (int)result);
        }
    }

    static double calc(int v) {

        if (op[v] == 0) {
            return val[v];
        }

        double l = calc(left[v]);
        double r = calc(right[v]);

        if (op[v] == '+') return l + r;
        if (op[v] == '-') return l - r;
        if (op[v] == '*') return l * r;
        if (op[v] == '/') return l / r;

        return 0;
    }
}
