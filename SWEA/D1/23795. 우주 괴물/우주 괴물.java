import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			int[][] arr = new int[N][N];
			int ar=0,ac=0;
			
			for(int i=0; i<N; i++) 
				for(int j=0; j<N; j++) {
					arr[i][j] = sc.nextInt();
					
					if(arr[i][j] == 2) {
						ar = i;
						ac = j;
							
					}
				}
			
			//공격배열
			int[] dr = {0,1,0,-1};
			int[] dc = {1,0,-1,0};
			
			boolean[][] attack=new boolean[N][N];
			
			//공격ㄱ
			for(int d=0; d<4; d++) {
				int nr = ar+dr[d];
				int nc = ac+dc[d];
				
				while(0<= nr && nr<N && 0<=nc && nc<N && arr[nr][nc] !=1) {	
					if(arr[nr][nc] ==0)	
						attack[nr][nc] = true;
					nr+=dr[d];
					nc +=dc[d];
				}
				
			}
			int cnt=0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(arr[i][j] ==0 && !attack[i][j]) cnt++;
				}
			}
			System.out.println("#"+tc+" "+cnt);
			
			
			
			
		}
	}
}