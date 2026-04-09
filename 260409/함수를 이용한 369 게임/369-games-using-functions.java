import java.util.Scanner;

class Main{
	static int cnt;
	static int a,b;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		a = sc.nextInt();
		b = sc.nextInt();
		
		cnt=0;
		check(a,b);
		
	}
	static void check(int x, int y) {
		for(int i=x; i<=y; i++) {
			String s = String.valueOf(i);
			if(s.contains("3") ||s.contains("6")  ||s.contains("9")) {
				cnt++;
			}else if(i%3==0) cnt++;
		}
		System.out.println(cnt);
	}
}