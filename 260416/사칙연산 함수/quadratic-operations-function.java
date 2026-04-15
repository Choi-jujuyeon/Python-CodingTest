import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		String o = sc.next();
		int b = sc.nextInt();
		
		int result = 0;
		boolean flag = true;
		
		switch(o) {
		case "+":
			result = add(a, b);
			break;
		case "-":
			result = sub(a, b);
			break;
		case "*":
			result = mul(a, b);
			break;
		case "/":
			result = div(a, b);
			break;
		default:
			flag = false;
		}
		
		if(flag) {
			System.out.println(a + " " + o + " " + b + " = " + result);
		} else {
			System.out.println("False");
		}
	}
	
	// 덧셈
	static int add(int x, int y) {
		return x + y;
	}
	
	// 뺄셈
	static int sub(int x, int y) {
		return x - y;
	}
	
	// 곱셈
	static int mul(int x, int y) {
		return x * y;
	}
	
	// 나눗셈 (정수 나눗셈)
	static int div(int x, int y) {
		return x / y;
	}
}