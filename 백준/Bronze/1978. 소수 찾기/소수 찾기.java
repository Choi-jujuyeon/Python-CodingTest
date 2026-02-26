import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int cnt=0;
		for(int i=0; i<N; i++) {
			boolean f = true;
			int num = sc.nextInt();
			if (num < 2) continue;
			for(int j=2; j<num; j++) {
				if(num%j==0) {
					f=false;
					break;
				}
			}
			if(f) cnt+=1;

		}
		System.out.println(cnt);
	}
}