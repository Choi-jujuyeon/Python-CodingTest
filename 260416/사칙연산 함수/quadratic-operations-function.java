import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		String o = sc.next();
		int b = sc.nextInt();
		
		
		switch(o) {
		case "+":
			System.out.println(a+b);
			break;
		case "-":
			System.out.println(a-b);
			break;
		case "*":
			System.out.println(a*b);
            break;
		case "/":
			System.out.println(a/b);
            break;
		default:
			System.out.println("False");
            

		}
		
	}
}