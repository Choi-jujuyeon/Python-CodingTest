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
			 for(int i=0; i<M; i++) b[i] =sc.nextInt();
			 
			 int max = Integer.MIN_VALUE;
			 
			 //M길이가 항상 큰 길이로 가정하기!
			 if(N>M) {
				 int[] tmp = a; a=b; b=tmp;
				 int t=N; N=M; M=t;
			 }
			 for(int i=0; i<=M-N; i++) {
				 int sum=0;
				 for(int j=0; j<N; j++) {
					 sum+=a[j] * b[i+j];
				 }
				 if(sum>max) max=sum;
			 }
			 System.out.println("#"+tc+" "+max);
				
		 }
		
	}
}