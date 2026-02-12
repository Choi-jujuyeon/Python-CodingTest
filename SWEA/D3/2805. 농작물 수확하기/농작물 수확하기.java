import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T=sc.nextInt();
		
		for(int tc =1; tc<=T; tc++) {
			
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			
			for(int i=0; i<N; i++) {
				String line = sc.next(); 
				for(int j=0; j<N; j++)
					arr[i][j] = line.charAt(j) -'0';
			}
			//별찍기 느낌으로 ㄱㄱ
			
			int mid = N / 2;
			int sum = 0;
			
			// 별찍기처럼 위에서 아래로 한 줄씩
			for (int r = 0; r < N; r++) {
				int gap = Math.abs(r - mid);
				int start = gap;
				int end = N - 1 - gap;
				
				for (int c = start; c <= end; c++) {
					sum += arr[r][c];
				}
			}
			
			System.out.println("#" + tc + " " + sum);
		}
    }
}