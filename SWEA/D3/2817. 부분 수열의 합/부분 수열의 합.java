import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution{
	static int K,N;
	static int cnt;
	static int[] arr;
	
	static void check(int idx, int sum) {
		if(sum > K) return;
		
		if(idx==N) {
			if(sum==K) cnt++;
			return;
		}
		
		//포함
		check(idx+1, sum+arr[idx]);
		//불포함
		check(idx+1, sum);
		
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int T = Integer.parseInt(br.readLine().trim());
		for(int tc=1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			st=new StringTokenizer(br.readLine());
			arr = new int[N];
			for(int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());
			
			cnt=0;
			check(0,0);
			
			System.out.println("#"+tc+" "+cnt);
		}
		
		
	}
}