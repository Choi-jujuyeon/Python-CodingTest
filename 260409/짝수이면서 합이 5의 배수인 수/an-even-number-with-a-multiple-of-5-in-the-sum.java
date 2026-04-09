import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		check(T);
		
	}
	static void check(int x) {
		if(x%2==0) {
			int tmp =0;
			while(x>0) {
				tmp += x%10;
				x = x/10;
			}
			if(tmp%5 ==0) System.out.println("Yes");
		}
		else
			System.out.println("No");
	}
}