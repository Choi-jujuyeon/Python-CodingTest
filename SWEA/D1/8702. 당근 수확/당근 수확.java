import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc =1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			int[] arr = new int[N];
			int total=0;
			
			for(int i=0; i<N; i++) {
				arr[i] = sc.nextInt();
				total+=arr[i];
			}
			
			int left =0;
			int min = Integer.MAX_VALUE;
			int idx=0;
			
			for(int i=0; i<N-1; i++) {
				left+=arr[i];
				int right=total-left;
				
				if(min> Math.abs(right-left)) {
					min = Math.abs(right-left);
					idx = i+1;
				}
			}
			
			
			System.out.println("#"+tc+" "+idx+" "+min);
		}
	}
}