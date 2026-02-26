import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for(int i = 0; i < T; i++) {
            int num = sc.nextInt();
            String s = sc.next();

            StringBuilder sb = new StringBuilder();

            for(int j = 0; j < s.length(); j++) {
                for(int k = 0; k < num; k++) {
                    sb.append(s.charAt(j));
                }
            }

            System.out.println(sb.toString());
        }

        sc.close();
    }
}