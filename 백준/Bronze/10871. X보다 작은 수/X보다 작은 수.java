import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int X = sc.nextInt();
		for(int i=0; i<N; i++) {
			int num =sc.nextInt();
			if(X>num)
				System.out.print(num+" ");		
		}
	}
}