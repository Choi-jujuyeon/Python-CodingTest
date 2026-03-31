import java.util.Scanner;

class Main{
	
	static int a,b;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		a = sc.nextInt();
		b = sc.nextInt();
		int ans =check(a,b);
		System.out.println(ans+"\n"+ans * (a/ans) * (b/ans));
		
	}
	static int check(int n, int m) {
		if(m==0) return n;
		return check(m, n%m);
	}
}