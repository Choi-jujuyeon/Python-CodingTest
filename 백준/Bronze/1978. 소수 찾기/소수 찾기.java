import java.util.Scanner;

class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int ans =0;
		for(int i=0; i<N; i++) {
			int tmp = sc.nextInt();
			
			//소수조건
			boolean flag = true;
			if(tmp==1) continue;
			for(int j=2; j<tmp; j++) {
				if(tmp%j==0) flag = false; 
			}
			if(flag) ans++;
		}
		 System.out.println(ans);
	}
}