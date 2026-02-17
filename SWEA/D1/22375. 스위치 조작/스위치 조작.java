import java.util.Scanner;

class Solution{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			int[] a= new int[N];
			int[] b= new int[N];
			for(int i=0; i<N; i++) a[i]=sc.nextInt() ;
			for(int i=0; i<N; i++) b[i]=sc.nextInt() ;
			
			int[] result = new int[N];
			for(int i=0; i<N; i++) {
				result[i] = a[i] ^ b[i];
			}
			
			int check=result[0];
			int cnt = (check == 1) ? 1 : 0;			
            for(int i=1; i<N; i++) {
				if(result[i]!= check) {
					cnt++;
					check=result[i];
				}
			}
			
			System.out.println("#"+tc + " "+ cnt);
		}
	}
}