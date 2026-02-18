import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			//미리 행 열 합 구해두기!
			int[] rowSum = new int[N];
			int[] colSum = new int[N];
			
			int[][] arr = new int[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					arr[i][j] = sc.nextInt();
					rowSum[i] +=arr[i][j];
					colSum[j] +=arr[i][j];
				}
			}
			
			int max=Integer.MIN_VALUE;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					int check = rowSum[i] + colSum[j] - arr[i][j];
					if(check>max) max=check;
				}
			}
			System.out.println("#"+tc+" "+max);
			
			
		}
	}
}