import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		String s = sc.next();
		int ans =0;
		for(int i=0; i<a; i++) {
			ans += s.charAt(i) - '0';
		}
		System.out.println(ans);
	}
}