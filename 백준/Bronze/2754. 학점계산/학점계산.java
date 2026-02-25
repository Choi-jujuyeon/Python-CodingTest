import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		double ans = 0.0;
		
		switch(s) {
			case "A+":
				ans = 4.3;
				break;
			case "A0":
				ans = 4.0;
				break;
			case "A-":
				ans = 3.7;
				break;
				
			case "B+":
				ans = 3.3;
				break;
			case "B0":
				ans = 3.0;
				break;
			case "B-":
				ans = 2.7;
				break;
				
			case "C+":
				ans = 2.3;
				break;
			case "C0":
				ans = 2.0;
				break;
			case "C-":
				ans = 1.7;
				break;
				
			case "D+":
				ans = 1.3;
				break;
			case "D0":
				ans = 1.0;
				break;
			case "D-":
				ans = 0.7;
				break;
				
			case "F":
				ans = 0.0;
				break;
		}
		
		System.out.println(ans);
	}
}