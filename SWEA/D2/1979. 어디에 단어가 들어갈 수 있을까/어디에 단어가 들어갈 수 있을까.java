import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N=sc.nextInt();
			int K = sc.nextInt();
			
			int[][] arr = new int[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			int cnt=0;
			//가로행체크
			for(int i=0; i<N; i++) {
				int len=0;
				for(int j=0; j<N; j++) {
					if(arr[i][j] ==1) len++;
					else {
						if(len == K) cnt++;
						len=0;
					}
				}
				if(len == K ) cnt++;
			}
			
			//세로열체크
			for(int i=0; i<N; i++) {
				int len=0;
				for(int j=0; j<N; j++) {
					if(arr[j][i] ==1) len++;
					else {
						if(len == K) cnt++;
						len=0;
					}
				}
				if(len == K ) cnt++;
			}
            System.out.println("#" + tc + " " + cnt);

		}
				
	}
}