import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		for(int tc=1; tc<=10; tc++) {
			int T = sc.nextInt();
			
			int C = sc.nextInt();
			int N = sc.nextInt();

			System.out.println("#"+tc+" "+check(C,N));
		}
	}
	static int check(int c, int n) {
		if(n==0) return 1;
		
		int tmp = check(c, n/2);
		if(n%2 ==1) return tmp * tmp*c;
		
		return tmp *tmp;
	}
}