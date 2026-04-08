import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc =1; tc<=T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			boolean[][] arr = new boolean[N+1][N+1];
			for(int i=0; i<M; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				
				arr[a][b] = true;
			}
			
			//플로이드
			for(int k=1; k<=N; k++) {
				for(int i=1; i<=N; i++) {
					for(int j=1; j<=N; j++) {
						if(arr[i][k] && arr[k][j]) {
							arr[i][j] = true;
						}
					}
				}
			}
			
			int ans =0;
			for(int i=1; i<=N; i++) {
				int cnt=0;
				for(int j=1; j<=N; j++) {
					if(i==j) continue;
					if(arr[i][j] || arr[j][i]) cnt++;
				}
				if(cnt == N-1) ans++;
			}
			

			System.out.println("#" + tc + " " + ans);
			
		}
	}
}