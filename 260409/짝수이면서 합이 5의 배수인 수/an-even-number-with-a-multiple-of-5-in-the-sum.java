import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		check(T);
		
	}
	static void check(int x) {
		int n = x;
		int tmp =0;
		while(x>0) {
			tmp += x%10;
			x = x/10;
		}
		System.out.println((n%2==0 && tmp%5==0)?"Yes":"No" );
	}
}