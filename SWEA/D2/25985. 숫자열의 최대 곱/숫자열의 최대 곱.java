import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<T+1; tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			int[] a = new int[N];
			int[] b = new int[M];
			
			for(int i=0; i<N; i++) a[i]= sc.nextInt();
			for(int i=0; i<M; i++) b[i] = sc.nextInt();
			
			int max=Integer.MIN_VALUE;

			for(int k=-(M-1); k<=N-1; k++) {
				int sum =0;
				
                for (int i = 0; i < N; i++) {
                    int j = i - k; 
                    if (0 <= j && j < M) {
                        sum += a[i] * b[j];
                    }
                }
				if(max<sum) max=sum;
			}
			System.out.println("#"+tc +" "+max);				
		}
	}
}