import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int y = sc.nextInt();
		
		System.out.println(check(y));
		
	}
	static boolean check(int x) {
		if( x%400==0 || (x%4 ==0 && x%100!=0)) return true;
		
		else return false;
	}
}