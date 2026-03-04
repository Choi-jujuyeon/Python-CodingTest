import java.util.Scanner;

class Solution{
	static int cnt;
	static void check(long n) {
		if(n==2) return;
		
		long l = (long)Math.sqrt(n);
		if(l*l == n) {
			cnt++;
			check(l);
		}else {
			long next = l+1;
            cnt += (next * next - n); 
            check(next * next);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T =sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			long N = sc.nextLong();
			cnt =0;
			check(N);
			System.out.println("#"+tc+" "+cnt);
		}
	}
}