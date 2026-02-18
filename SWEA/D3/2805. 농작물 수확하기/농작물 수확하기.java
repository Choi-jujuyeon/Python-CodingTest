import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			int[][] arr = new int[N][N];
			for(int i=0; i<N; i++) {
				String s = sc.next();
				for(int j=0; j<s.length(); j++) {
					arr[i][j] = s.charAt(j)-'0';
				}
			}
			
			int mid = N/2;
			int result =0;
			
			for(int r=0; r<N; r++) {
				int gap = Math.abs(r-mid);
				int start = gap;
				int end = N-1-gap;						
				
				for(int c=start; c<=end; c++) {
					result+=arr[r][c];
				}
			}
			System.out.println("#"+tc+" "+result);
		}
	}
}