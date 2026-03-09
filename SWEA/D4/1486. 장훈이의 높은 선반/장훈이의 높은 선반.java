import java.util.Scanner;

class Solution{
	static int N,B;
	static int[] arr;
	static int ans;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			B= sc.nextInt();
			
			arr = new int[N];
			for(int i=0; i<N; i++) arr[i] =sc.nextInt();
			ans = Integer.MAX_VALUE;
			
			check(0,0);
			System.out.println("#"+tc+" "+ans);
		}
	}
	static void check(int idx, int sum) {
		if(sum>=B) {
			ans = Math.min(ans, sum-B);
		}
		if(idx==N) return;
		check(idx+1, sum+arr[idx]);
		check(idx+1, sum);
	}
}