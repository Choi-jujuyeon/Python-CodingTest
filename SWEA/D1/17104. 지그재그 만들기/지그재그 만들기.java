class Solution{
	public static void main(String[] args) {
		int N = 10;
		int[][] arr = new int[N][N];
		int num =1;
		
		for(int i=0; i<N; i++) {

			for(int j=0; j<N; j++) {
				int col=0;
				
				//짝수일경우
				if(i%2==0) col=j; 
				//홓수
				else col =N-1-j;
				
				arr[i][col] = num;
				num++;
				
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		
				
	}
}