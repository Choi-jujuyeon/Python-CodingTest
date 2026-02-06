import java.util.Scanner;

public class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int tc=1; tc<11; tc++) {
			sc.nextInt();
			 int a = sc.nextInt();
			 int b = sc.nextInt();
			System.out.println("#"+tc+" "+check(a,b));
		}
	}
	
	public static int check(int a, int b) {
		//basecase*
		if(b==0)
			return 1;
		
		return a*check(a,b-1);
	}
}