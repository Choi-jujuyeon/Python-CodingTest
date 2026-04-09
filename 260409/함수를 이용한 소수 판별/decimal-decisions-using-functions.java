import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		check(a,b);
	}
	static void check(int x, int y) {
		int cnt =0; 
		
		for(int i=x; i<=y; i++) {
			boolean flag = true;
			if(i<2) flag = false;
			for(int j=2; j<i; j++) {
				if(i%j==0) {
					flag = false;
					break;
				}
			}
			if(flag) cnt+=i;
			
		}
		System.out.println(cnt);
	}
	
}