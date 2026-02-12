import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T;tc++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			int[] a = new int[N];
			int[] b = new int[M];
			
			for(int i=0; i<N; i++) a[i]=sc.nextInt();
			for(int i=0; i<M; i++) b[i]=sc.nextInt();
			
			//n이 항상 작게 설정
			if(N>M) {
				int[] tmp=a; a=b; b=tmp;
				int t=N; N=M; M=t;
			}
			int max=0;
			//이동
			 for(int i=0; i<=M-N; i++) {
				 int sum=0;
				 for(int j=0; j<N; j++) {
					 sum+=a[j]*b[j+i];
				 }
				 if(max<sum) max=sum;
			 }
			 System.out.println("#"+tc+ " "+max);
		}
	}
}