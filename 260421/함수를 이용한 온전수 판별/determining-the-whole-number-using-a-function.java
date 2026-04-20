import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt();
		int B = sc.nextInt();
		
		System.out.println(check(A,B));
		
	}
	static int check(int a, int b) {
		int cnt =0;
		for(int i=a; i<=b; i++) {
			if(i%2==0 || i%10 == 5 || (i%3==0 && i%9!=0)) {
				continue;
			}else cnt++;
		}
		return cnt;
	}
}