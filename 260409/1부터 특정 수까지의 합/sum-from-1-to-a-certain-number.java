import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		check(T);
	}
	static void check(int x) {
		int sum =0;
		for(int i=1; i<=x; i++ ) sum+=i;
		System.out.println(sum/10);
	}
}