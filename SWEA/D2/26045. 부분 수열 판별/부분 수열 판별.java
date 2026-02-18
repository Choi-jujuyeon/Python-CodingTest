import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			int[] arrN = new int[N];
			int[] arrM = new int[M];
			
			for(int i=0; i<N; i++) arrN[i] =sc.nextInt();
			for(int j=0; j<M; j++) arrM[j] = sc.nextInt();
			
			int idx=0;
			boolean result = false;
			
			for(int i=0; i<M; i++) {
				result=false;
				for(int j=idx; j<N; j++) {
					if(arrM[i]== arrN[j]) {
						idx=j+1;
						result=true;
						break;
					}
				}
				if(!result) break; 
			}
			
			System.out.println("#"+tc+" "+(result?"YES":"NO"));
		}
	}
}