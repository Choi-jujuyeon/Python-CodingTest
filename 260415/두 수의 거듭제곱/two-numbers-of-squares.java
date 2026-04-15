import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		System.out.println(check(a,b));
	}
	static int check(int x, int y) {
		int ans = 1;
		for(int i=0; i<y; i++) {
			ans *= x;
		}
		return ans;
	}
}