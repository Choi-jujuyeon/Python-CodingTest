import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t=1; t<=T; t++) {
			int N =sc.nextInt();
			int M =sc.nextInt();
			int[][] arr = new int[N][N];
			
			for(int j=0; j<N; j++) {
				for(int k=0; k<N; k++) {
					arr[j][k]=sc.nextInt();
				}
			}
//			System.out.println(Arrays.deepToString(arr));
			int max =0;
			
			for(int i=0; i<=N-M; i++) {
				for(int j=0; j<=N-M; j++) {
					int sum =0;
					
					for(int p=i; p<i+M; p++) {
						for(int q=j; q<j+M; q++) {
							sum+=arr[p][q];
						}
					}
					if(sum>max)
						max=sum;
				}
			}
            System.out.println("#" + t + " " + max);
		}	
	}
}