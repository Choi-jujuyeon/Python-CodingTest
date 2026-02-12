import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<T+1; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();	//이게 숫자
			
			String b = Integer.toBinaryString(M);
			boolean check= true;
			int len = b.length();
			
			if(N>len) check=false;
			else{
				for(int i=len-1; i>=len-N; i--) {
			
					if(b.charAt(i) !='1') {
						check=false;
						break;
					}
				}
			}
			System.out.println("#"+tc+" "+(check? "ON": "OFF"));
		}
	}
}