import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[6];

        for(int i=0; i<6; i++) arr[i] = sc.nextInt();
        int T = sc.nextInt();
        int P = sc.nextInt();

        long tCnt = 0;
        for(int i=0; i<6; i++) {
            tCnt += (arr[i] + T - 1) / T;  
        }

        System.out.println(tCnt);
        System.out.println((N / P) + " " + (N % P));
    }
}