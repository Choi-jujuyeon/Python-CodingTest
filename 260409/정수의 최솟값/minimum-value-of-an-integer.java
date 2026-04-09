import java.util.Arrays;
import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		check(a,b,c);
		
	}
	static void check(int a, int b, int c) {
		int[] arr = {a,b,c};
		Arrays.sort(arr);
		
		System.out.println(arr[0]);
		
	}
}